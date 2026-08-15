#!/bin/bash

# Path to the blog log
BLOG_LOG="_data/blog-log.md"

# End date (current date from context)
END_DATE="2026-08-14"
# Minimum number of posts desired
MIN_POSTS=300

# Find the last date in the blog log to avoid duplicating posts
LAST_DATE=$(grep '^## ' "$BLOG_LOG" | tail -1 | sed 's/^## //')
# If the blog log is empty, start from a default date
if [ -z "$LAST_DATE" ]; then
    START_DATE="2025-09-12"
else
    START_DATE=$(date -d "$LAST_DATE + 1 day" +%Y-%m-%d)
fi

# Function to count blog log entries
count_posts() {
    grep -c '^## ' "$BLOG_LOG"
}

# Current date
CURRENT_DATE="$START_DATE"

echo "Starting from $CURRENT_DATE, ending at $END_DATE"
echo "Minimum posts desired: $MIN_POSTS"

while [ "$CURRENT_DATE" != "$END_DATE" ]; do
    # Check if we have enough posts
    POST_COUNT=$(count_posts)
    if [ $POST_COUNT -ge $MIN_POSTS ]; then
        echo "Reached minimum post count ($POST_COUNT). Stopping."
        break
    fi

    echo "Processing date: $CURRENT_DATE (current posts: $POST_COUNT)"

    # Generate the post for this date
    python3 generate_post.py "$CURRENT_DATE"
    if [ $? -ne 0 ]; then
        echo "Failed to generate post for $CURRENT_DATE. Exiting."
        break
    fi

    # Determine the generated file name (we can infer from the script, but let's just add the log and the post)
    # The script generates a post in _posts with the pattern YYYY-MM-DD-ai-*.md
    # We'll add all new posts in _posts and the blog log
    git add _posts/${CURRENT_DATE}-ai-*.md "$BLOG_LOG"
    if [ $? -ne 0 ]; then
        echo "Failed to stage files for $CURRENT_DATE. Exiting."
        break
    fi

    # Commit
    git commit -m "$(cat <<EOF
Add AI blog post for $CURRENT_DATE

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
    if [ $? -ne 0 ]; then
        echo "Failed to commit for $CURRENT_DATE. Exiting."
        break
    fi

    # Increment date by one day
    CURRENT_DATE=$(date -d "$CURRENT_DATE + 1 day" +%Y-%m-%d)
done

# After loop, check if we reached the end date
if [ "$CURRENT_DATE" = "$END_DATE" ]; then
    # Process the end date if we haven't already (loop stops when CURRENT_DATE equals END_DATE, so we need to process END_DATE)
    POST_COUNT=$(count_posts)
    if [ $POST_COUNT -lt $MIN_POSTS ]; then
        echo "Processing final date: $CURRENT_DATE (current posts: $POST_COUNT)"
        python3 generate_post.py "$CURRENT_DATE"
        if [ $? -eq 0 ]; then
            git add _posts/${CURRENT_DATE}-ai-*.md "$BLOG_LOG"
            git commit -m "$(cat <<EOF
Add AI blog post for $CURRENT_DATE

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
        fi
    fi
fi

echo "Done."
POST_COUNT=$(count_posts)
echo "Total posts in blog log: $POST_COUNT"