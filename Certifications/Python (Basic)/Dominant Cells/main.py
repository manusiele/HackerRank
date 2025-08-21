#!/bin/python3

import math
import os
import random
import re
import sys

def numCells(grid):
    if not grid or not grid[0]:
        return 0
    
    n = len(grid)
    m = len(grid[0])
    dominant_count = 0
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(n):
        for j in range(m):
            current_value = grid[i][j]
            is_dominant = True
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] >= current_value:
                    is_dominant = False
                    break
            
            if is_dominant:
                dominant_count += 1
    
    return dominant_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()