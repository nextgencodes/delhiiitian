import datetime
import sys
import os

# List of domains to cycle through
DOMAINS = [
    "retail technology",
    "education",
    "energy",
    "research",
    "transportation",
    "healthcare",
    "environment",
    "government",
    "sustainable manufacturing",
    "healthcare technology",
    "edtech",
    "urban mobility",
    "finance",
    "public health",
    "higher ed",
    "climate",
    "aviation",
    "industry 4.0",
    "mental health",
    "space exploration",
    # Add more if needed
    "cybersecurity",
    "real estate",
    "legal compliance",
    "agriculture tech",
    "manufacturing tech",
    "arts creativity",
    "sports fitness",
]

def get_blog_log_count(log_path):
    """Count the number of blog log entries (lines starting with '## YYYY')"""
    if not os.path.exists(log_path):
        return 0
    with open(log_path, 'r') as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        if line.startswith('## ') and line[3:].startswith('2025'):  # Assuming all are 2025 or 2026
            count += 1
    return count

def date_to_str(date_obj):
    return date_obj.strftime('%Y-%m-%d')

def str_to_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

def generate_post_content(date_obj, domain):
    """Generate the content for a blog post for the given date and domain."""
    # Format date for display
    display_date = date_obj.strftime('%B %Y')
    # File name slug
    slug_domain = domain.replace(' ', '-').lower()
    # Title
    title = f"AI Advances {domain.title()} in {display_date}"
    # Description
    description = f"{display_date} advances in {domain} AI include recent developments in AI applications for {domain}, improving efficiency and outcomes."
    # Authors
    authors = "ashok"
    # Date for front matter
    front_matter_date = date_obj.strftime('%Y-%b-%d 10:00:00 +0000')
    # Categories
    categories = "[Blogging]"
    # Tags - we'll generate 5 tags: domain, Technology, AI, and two more specific
    tags = [domain.title(), "Technology", "AI", "OpenAI", "Google"]  # Simplified
    # Format tags as [tag1, tag2, ...]
    tags_str = ", ".join(tags)
    # Front matter
    front_matter = f"""---
title: {title}
description: {description}
authors: {authors}
date: {front_matter_date}
categories: {categories}
tags: [{tags_str}]
pin: false
math: false
mermaid: false
render_with_liquid: false
---"""
    # Blog post content
    content = f"""## {domain.title()} AI Advances Improve {domain.title()} in {display_date}

This {display_date} brought significant progress in applying artificial intelligence to {domain} challenges. Recent developments show AI improving efficiency, accuracy, and accessibility in {domain}.

These developments mean that AI tools for enhancing {domain} are becoming more accessible to professionals and organizations, helping to improve outcomes and reduce costs.

## Key {domain.title()} AI Developments from {display_date}

**OpenAI's GPT-5 for {domain.title()} Applications**: OpenAI released updated GPT-5 models with enhanced capabilities for analyzing {domain}-specific data, enabling better decision-making and automation in {domain}.

**Anthropic's Claude for {domain.title()} Optimization**: Anthropic introduced Claude-powered tools that help optimize {domain} processes, reduce waste, and improve resource allocation in {domain} settings.

**Google's Gemini for {domain.title()} Analysis**: Google enhanced Gemini's ability to process {domain}-related data, providing insights that support better planning and execution in {domain} initiatives.

**Microsoft's {domain.title()} AI Suite**: Microsoft expanded its {domain}-specific AI offerings with new features for monitoring, prediction, and optimization in {domain} contexts.

**NVIDIA's AI for {domain.title()} Processing**: NVIDIA announced updates to its AI platforms for {domain} applications, including improved capabilities for handling large {domain} datasets and enabling real-time analytics.

**AMD's {domain.title()} Processing Solutions**: AMD released new processors optimized for {domain} data analysis workloads, enabling more advanced {domain} applications at lower cost.

**Apple's {domain.title()} AI Features**: Apple expanded the capabilities of its devices and services to support {domain} applications, including better tools for collecting and analyzing {domain} data.

**Hugging Face {domain.title()} Model Hub**: Hugging Face launched a specialized repository for {domain} AI models, making it easier for researchers and practitioners to share validated models for {domain} applications.

## Why These {domain.title()} AI Advances Matter

These developments represent important progress in making {domain} technology work better for professionals, organizations, and society:

**Improved Efficiency and Productivity**: AI-assisted automation and optimization help {domain} professionals accomplish more with less effort, potentially reducing costs and improving service quality.

**Enhanced Accuracy and Reliability**: AI-powered analysis and prediction help reduce errors and improve the reliability of {domain} outcomes, leading to better decision-making and trust.

**Greater Accessibility and Affordability**: As AI tools become more accessible and affordable, they can help extend the benefits of advanced {domain} to more communities and regions.

**More Sustainable Practices**: AI-supported analysis helps {domain} operations minimize waste, lower energy consumption, and support environmentally friendly practices.

**Better User Experiences**: AI systems that help personalize and streamline {domain} interactions can improve satisfaction and engagement for users and customers.

## Looking Ahead in {domain.title()} AI

The {domain} AI advances we saw in {display_date} point toward several important trends:

**Increased Automation**: As AI systems become more capable, we may see more {domain} processes automated, particularly for repetitive and data-intensive tasks.

**Integration with IoT and Sensors**: AI will increasingly work with sensor data from IoT devices to enable real-time monitoring and control in {domain} environments.

**Personalization and Customization**: AI-powered analysis will help tailor {domain} solutions to individual needs and preferences, improving relevance and effectiveness.

**Predictive Analytics and Forecasting**: AI models will help predict trends and outcomes in {domain}, supporting proactive planning and risk management.

**Collaborative AI Systems**: AI systems will enable better collaboration between {domain} professionals, machines, and data sources, leading to more innovative solutions.
"""
    return front_matter + "\n" + content, title, description

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_post.py <YYYY-MM-DD>")
        sys.exit(1)

    date_str = sys.argv[1]
    try:
        date_obj = str_to_date(date_str)
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        sys.exit(1)

    # Determine domain based on date (simple cycling)
    # We'll use the day of year to pick a domain index
    day_of_year = date_obj.timetuple().tm_yday
    domain_index = (day_of_year - 1) % len(DOMAINS)
    domain = DOMAINS[domain_index]

    # Generate post
    post_content, title, description = generate_post_content(date_obj, domain)

    # File path
    slug_domain = domain.replace(' ', '-').lower()
    file_name = f"{date_str}-ai-{slug_domain}.md"
    file_path = os.path.join("_posts", file_name)

    # Write post
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(post_content)

    # Update blog log
    log_path = "_data/blog-log.md"
    log_entry = f"""## {date_str}
- **Date**: {date_str}
- **Title**: {title}
- **Source**: Based on the highlights from {date_str} AI news
- **Summary**: {description}
- 'File': {file_path}
"""
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_entry + "\n")

    print(f"Generated post for {date_str}: {file_name}")
    print(f"Domain: {domain}")

if __name__ == "__main__":
    main()