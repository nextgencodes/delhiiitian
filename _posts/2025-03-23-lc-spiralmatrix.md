---
title: 54. Spiral Matrix
description: 
authors: ashok
date: 2025-mar-23 10:00:00 +0000
categories: [Leetcode, Spiral Matrix]
tags: [Leetcode]
pin: true
---

### Introduction
Today, we're diving into a classic matrix problem: **spiral matrix traversal**. Given a 2D matrix, our goal is to extract all its elements in a spiral path, starting from the top-left corner and moving clockwise.
Check the leetcode problem [here](https://leetcode.com/problems/spiral-matrix/)


### Problem Statement
Given an m x n matrix, return all elements of the matrix in spiral order.

**Example 1:**

```python
Input: matrix = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]
```
{: .nolineno}

**Example 2:**

```python
Input: matrix = [[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```
{: .nolineno}

**Constraints:**

```python
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
```
{: .nolineno}

Notice the pattern? We traverse right, then down, then left, then up, and repeat this process inwards until we've visited all elements.

### Python Solution

Here's an efficient Python function to achieve spiral matrix traversal:

```python

def spiral_matrix(matrix):
    """
    Traverses a matrix in spiral order and returns a list of elements.
    Args:
        matrix: A 2D list representing the matrix.
    Returns:
        A list containing all elements of the matrix in spiral order.
    """
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    spiral_order = []

    while top <= bottom and left <= right:
        # Traverse right (top row)
        for col in range(left, right + 1):
            spiral_order.append(matrix[top][col])
        top += 1

        # Traverse down (right column)
        for row in range(top, bottom + 1):
            spiral_order.append(matrix[row][right])
        right -= 1

        if top <= bottom and left <= right: # Check if there are more layers to traverse
            # Traverse left (bottom row)
            for col in range(right, left - 1, -1):
                spiral_order.append(matrix[bottom][col])
            bottom -= 1

            # Traverse up (left column)
            for row in range(bottom, top - 1, -1):
                spiral_order.append(matrix[row][left])
            left += 1

    return spiral_order
```

### Explanation

1.  **Initialization:**
    *   We first handle the edge case of an empty matrix. If the matrix is empty, we return an empty list.
    *   We get the number of `rows` and `cols` of the input `matrix`.
    *   We define four variables: `top`, `bottom`, `left`, and `right` to keep track of the boundaries of the current layer we are traversing. Initially, `top` and `left` are 0 (top-left corner), and `bottom` and `right` are the indices of the last row and column respectively (bottom-right corner).
    *   `spiral_order` is initialized as an empty list to store the elements in spiral order.

2.  **Spiral Traversal Loop:**
    *   The `while top <= bottom and left <= right:` loop continues as long as there are layers to traverse within the matrix. This condition ensures that we haven't crossed over the boundaries while spiraling inwards.

3.  **Traverse Right (Top Row):**
    *   `for col in range(left, right + 1):` iterates through the columns from `left` to `right` in the current `top` row.
    *   `spiral_order.append(matrix[top][col])` adds each element of the top row to our `spiral_order` list.
    *   `top += 1` moves the `top` boundary down by one row, as the top row is now processed.

4.  **Traverse Down (Right Column):**
    *   `for row in range(top, bottom + 1):` iterates through the rows from the updated `top` to `bottom` in the current `right` column.
    *   `spiral_order.append(matrix[row][right])` adds each element of the right column to `spiral_order`.
    *   `right -= 1` moves the `right` boundary left by one column, as the right column is now processed.

5.  **Conditional Traversal Left and Up:**
    *   `if top <= bottom and left <= right:`: This crucial condition checks if there are still rows and columns remaining to be traversed after moving right and down. This is necessary to prevent duplicate traversal in cases of non-square matrices or when we reach the center of the matrix.
    *   **Traverse Left (Bottom Row):**
        *   `for col in range(right, left - 1, -1):` iterates through the columns from `right` to `left` (in reverse order) in the current `bottom` row.
        *   `spiral_order.append(matrix[bottom][col])` adds each element of the bottom row to `spiral_order`.
        *   `bottom -= 1` moves the `bottom` boundary up by one row.
    *   **Traverse Up (Left Column):**
        *   `for row in range(bottom, top - 1, -1):` iterates through the rows from `bottom` to `top` (in reverse order) in the current `left` column.
        *   `spiral_order.append(matrix[row][left])` adds each element of the left column to `spiral_order`.
        *   `left += 1` moves the `left` boundary right by one column.

6.  **Return Result:**
    *   Finally, `return spiral_order` returns the list containing all elements in spiral order.

### Time and Space Complexity

*   **Time Complexity: O(M \* N)**, where M is the number of rows and N is the number of columns in the matrix. We visit each element of the matrix exactly once.
*   **Space Complexity: O(1)**, excluding the space required to store the output list. We are only using a constant amount of extra space for variables like `top`, `bottom`, `left`, `right`, and loop counters. If we consider the output list, the space complexity is **O(M \* N)** to store all the elements in the `spiral_order` list.

### Conclusion

This Python solution efficiently traverses a matrix in spiral order by systematically shrinking the boundaries of the matrix layer by layer. It's a clear and concise approach that directly simulates the spiral path. Understanding this algorithm is a valuable step in mastering matrix manipulations and algorithmic thinking.

Feel free to experiment with different matrices and see the spiral traversal in action! Let me know in the comments if you have any questions or other interesting matrix problems you'd like to explore. Happy coding!
