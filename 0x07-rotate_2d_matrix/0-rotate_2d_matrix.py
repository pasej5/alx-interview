#!/usr/bin/env python3
"""_do not return anything matrix must be edited in place
"""

def rotate_2d_matrix(matrix):
    """
    Rotate 2D Matrix
    """
    left, right = 0, len(matrix[0]) - 1
    
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            
            # save the topleft value
            topLeft = matrix[top][left + i]
            
            # move the bottom left into the top left
            matrix[top][left + i] = matrix[bottom - i][left]
            
            # move the bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            
            # move the top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            
            # move top left to top right
            matrix[top + i][right] = topLeft
        
        right -= 1
        left += 1