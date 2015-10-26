import pprint
from enum import Enum
class Direction(Enum):
    left = 1
    down = 2
    up = 3
    right = 4

spiral = [[None for i in range(5)] for j in range(5)]

current_x, current_y = 0, 4
#initially moving to the left
move_x, move_y = 0, -1
current_dir = Direction.left
for i in range(25,0,-1):
    spiral[current_x][current_y] = i
    pprint.pprint(spiral)
    if current_y == 0 and current_dir == Direction.left:
        move_x = 1
        move_y = 0
        current_dir = Direction.down
    if current_x == 4 and current_dir == Direction.down:
        move_x = 0
        move_y = 1
        current_dir = Direction.right
        print('moving right')
    if current_y == 4 and current_dir == Direction.right:
        move_x = -1
        move_y = 0
        current_dir = Direction.up

        print('moving up')
    if current_x == 4 and current_dir == Direction.up:
        move_x = 0
        move_y = -1
        current_dir = Direction.left

    current_x += move_x
    current_y += move_y
    print(current_x,current_y,move_x,move_y)