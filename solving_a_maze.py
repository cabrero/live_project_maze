#!/usr/bin/env python3


import sys
from enum import Enum

filepath = sys.argv[1]

begin = 'o'
end   = 'x'
wall  = '*'

class Facing(Enum):
    North = 'North'
    East = 'East'
    South = 'South'
    West = 'West'

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

# Solve the maze
turns = {
    Facing.North: [Facing.East, Facing.North, Facing.West, Facing.South],
    Facing.East:  [Facing.South, Facing.East, Facing.North, Facing.West],
    Facing.South: [Facing.West, Facing.South, Facing.East, Facing.North],
    Facing.West:  [Facing.North, Facing.West, Facing.South, Facing.East],
}
def move(xy, facing):
    x, y = xy
    if facing == Facing.North:
        return (x, y-1)
    elif facing == Facing.East:
        return (x+1, y)
    elif facing == Facing.South:
        return (x, y+1)
    elif facing == Facing.West:
        return (x-1, y)
    
for row in maze:
    print("".join(row))
print()

xy = begin_xy
facing = Facing.North
print(f"Current position: {xy}")    

journey = [[None if cell == wall else set() for cell in row] for row in maze]

is_stuck = False
while xy != end_xy and not is_stuck:
    print(f"At {xy} facing {facing.value}")
    has_moved = False
    for f in turns[facing]:
        x, y = xy
        cell = journey[y][x]
        x_ , y_ = move(xy, f)
        if f not in cell and journey[y_][x_] is not None:
            cell.add(f)
            xy = (x_, y_)
            facing = f
            has_moved = True
            break
    is_stuck = not has_moved
    
if xy == end_xy:
    print(f"Exit at {xy}")
else:
    print("Couldn't find any solution 😢")
