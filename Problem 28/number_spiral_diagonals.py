import pprint
from enum import Enum
class Direction(Enum):
    left = 1
    down = 2
    up = 3
    right = 4


def create_spiral(size):
    spiral = [[0 for i in range(5)] for j in range(5)]
    current_x, current_y = 0, 4
    # initially moving to the left
    move_x, move_y = 0, -1
    current_dir = Direction.left
    for i in range(25, 0, -1):
        spiral[current_x][current_y] = i
        if current_dir == Direction.left and (
                    current_y + move_y < 0 or spiral[current_x + move_x][current_y + move_y] != 0):
            move_x = 1
            move_y = 0
            current_dir = Direction.down
        elif current_dir == Direction.down and (
                    current_x + move_x > 4 or spiral[current_x + move_x][current_y + move_y] != 0):
            move_x = 0
            move_y = 1
            current_dir = Direction.right
        elif current_dir == Direction.right and (
                    current_y + move_y > 4 or spiral[current_x + move_x][current_y + move_y] != 0):
            move_x = -1
            move_y = 0
            current_dir = Direction.up
        elif current_dir == Direction.up and (
                    current_x + move_x < 0 or spiral[current_x + move_x][current_y + move_y] != 0):
            move_x = 0
            move_y = -1
            current_dir = Direction.left
        current_x += move_x
        current_y += move_y
        pprint.pprint(spiral)
        print(current_x, current_y, move_x, move_y, spiral[current_x][current_y], current_dir)


create_spiral()



