'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
'''


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        width = len(grid)
        perimeter = 0
        for m in range(length):
            for n in range(width):
                if grid[n][m] == 1:
                    perimeter += 4
                    if n > 0 and grid[n-1][m] == 1: perimeter -= 1
                    if n < width-1 and grid[n+1][m] == 1: perimeter -= 1
                    if m > 0 and grid[n][m-1] == 1: perimeter -= 1
                    if m < length-1 and grid[n][m+1] == 1: perimeter -= 1
        return perimeter