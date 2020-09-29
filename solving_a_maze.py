#!/usr/bin/env python3


import sys

filepath = sys.argv[1]

begin = 'o'
end   = 'x'
wall  = '*'

# Read maze data from file
with open(filepath, 'r') as f:
    maze = [list(line.strip().lower()) for line in f if not line.isspace()]
begin_xy = None
end_xy = None

# Check maze data 
assert maze
cols = len(maze[0])
for y, row in enumerate(maze):
    assert len(row) == cols
    if begin in row:
        begin_xy = (row.index(begin), y)
    if end in row:
        end_xy = (row.index(end), y)
assert begin_xy
assert end_xy


