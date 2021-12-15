"""
Disclaimer: not entirely my solution!
"""

import heapq
import fileinput


def neighbors(x, y, a):
    r = len(a)
    c = len(a[0])
    dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return [(x+dx, y+dy) for dx, dy in dxdy if 0 <= x+dx < r and 0 <= y+dy < c]


def expand_grid(grid):
    rows, cols = len(grid), len(grid[0])
    big_grid = []
    for y in range(rows * 5):
        row = []
        for x in range(cols * 5):
            bx, by = x % cols, y % rows
            x_offset = x // cols
            y_offset = y // rows
            new_val = grid[y % cols][x % rows] + (x // cols) + (y // rows)
            while new_val > 9:
                new_val -= 9
            row.append(new_val)
        big_grid.append(row)
    return big_grid



def dijkstra(grid):
    start = (0, 0)
    end = (len(grid[0])-1, len(grid)-1)
    dist_heap = [(0, start)]
    visited = set()

    while dist_heap:
        dist, curr = heapq.heappop(dist_heap)
        if curr in visited:
            continue
        visited.add(curr)
        if curr == end:
            return dist

        for n in neighbors(curr[0], curr[1], grid):
            # Python's heapq can't update positions, so just push
            # everything and skip any repeats when popping
            n_cost = grid[n[1]][n[0]] + dist
            heapq.heappush(dist_heap, (n_cost, n))

grid = []
with open("Input.txt", mode='r') as f:
    lines = f.readlines()
for l in lines:
    if '\n' in l:
        l = l[:-1]
    grid.append(list(map(int, list(l))))

print(dijkstra(grid))

print(grid)
big_grid = expand_grid(grid)
print(dijkstra(big_grid))





