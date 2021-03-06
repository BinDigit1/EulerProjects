import pprint, time
from enum import Enum


class Direction(Enum):
    left = 1
    down = 2
    up = 3
    right = 4


class MySpiral:
    def __init__(self, size):
        self.size = size
        self.spiral = [[0 for i in range(size)] for j in range(size)]
        current_x, current_y = 0, size - 1
        # initially moving to the left
        move_x, move_y = 0, -1
        current_dir = Direction.left
        for i in range(size * size, 0, -1):
            self.spiral[current_x][current_y] = i
            if current_dir == Direction.left and (
                                current_y + move_y < 0 or self.spiral[current_x + move_x][current_y + move_y] != 0):
                move_x = 1
                move_y = 0
                current_dir = Direction.down
            elif current_dir == Direction.down and (
                                current_x + move_x > size - 1 or self.spiral[current_x + move_x][
                            current_y + move_y] != 0):
                move_x = 0
                move_y = 1
                current_dir = Direction.right
            elif current_dir == Direction.right and (
                                current_y + move_y > size - 1 or self.spiral[current_x + move_x][
                            current_y + move_y] != 0):
                move_x = -1
                move_y = 0
                current_dir = Direction.up
            elif current_dir == Direction.up and (
                                current_x + move_x < 0 or self.spiral[current_x + move_x][current_y + move_y] != 0):
                move_x = 0
                move_y = -1
                current_dir = Direction.left
            current_x += move_x
            current_y += move_y
            # pprint.pprint(spiral)
            # print(current_x, current_y, move_x, move_y, spiral[current_x][current_y], current_dir)

    def sum_first_diagonal(self):
        return sum(self.spiral[i][i] for i in range(0, self.size))

    def sum_second_diagonal(self):
        return sum(self.spiral[i][self.size - 1 - i] for i in range(0, self.size))

    def diagonal_sum(self):
        # note that the central 1 is counted twice
        return self.sum_first_diagonal() + self.sum_second_diagonal() - 1

    def print_me(self):
        pprint.pprint(self.spiral)


start_time = time.time()
a_spiral = print(MySpiral(1001).diagonal_sum())
print("--- %s seconds ---" % (time.time() - start_time))
