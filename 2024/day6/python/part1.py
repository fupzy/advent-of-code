# pylint: disable=bad-indentation

"""
Advent of Code Day 6 Part 1.
"""

import copy

RELATIVE_PATH = "../inputs/input.txt"
RELATIVE_PATH_TEST = "../inputs/short.txt"

def solution():
  """Solution"""

  map_matrix = []

  with open(RELATIVE_PATH_TEST, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      matrix_line = []
      for letter in line:
        if letter != '\n':
          matrix_line.append(letter)
      map_matrix.append(matrix_line)

  res = compute_guard_path(map_matrix)

  return count_guard_pos(res)

def compute_guard_path(mapp):
  """Compute guard path"""

  guard_symbol = '^'

  new_map = copy.deepcopy(mapp)

  x_init, y_init = get_guard_pos(mapp, guard_symbol)
  new_map[x_init][y_init] = 'X'

  while True:
    match guard_symbol:
      case '^':
        next_x, next_y = x_init - 1, y_init

        if not is_in_map(mapp, next_x, next_y):
          return new_map
        else :
          if mapp[next_x][next_y] == '#':
            guard_symbol = '>'
          else :
            new_map[next_x][next_y] = 'X'
            x_init, y_init = next_x, next_y
      case '>':
        next_x, next_y = x_init, y_init + 1
        if not is_in_map(mapp, next_x, next_y):
          return new_map
        else :
          if mapp[next_x][next_y] == '#':
            guard_symbol = 'v'
          else :
            new_map[next_x][next_y] = 'X'
            x_init, y_init = next_x, next_y

      case '<':
        next_x, next_y = x_init, y_init - 1
        if not is_in_map(mapp, next_x, next_y):
          return new_map
        else :
          if mapp[next_x][next_y] == '#':
            guard_symbol = '^'
          else :
            new_map[next_x][next_y] = 'X'
            x_init, y_init = next_x, next_y

      case 'v':
        next_x, next_y = x_init + 1, y_init
        if not is_in_map(mapp, next_x, next_y):
          return new_map
        else :
          if mapp[next_x][next_y] == '#':
            guard_symbol = '<'
          else :
            new_map[next_x][next_y] = 'X'
            x_init, y_init = next_x, next_y

  return new_map

def count_guard_pos(mapp):
  """Count all the guard positions"""

  guard_pos_symbol = 'X'
  lines = len(mapp)
  columns = len(mapp[0])
  counter=0

  for i in range(lines):
    for j in range(columns):
      if mapp[i][j] == guard_pos_symbol:
        counter +=1

  return counter

def is_in_map(mapp, i, j):
  """Returns true if i and j are mapp indexes"""

  lines = len(mapp)
  columns = len(mapp[0])

  return i >= 0 and i < lines and j >= 0 and j < columns

def get_guard_pos(mapp, symbol):
  """Returns the guard position"""

  lines = len(mapp)
  columns = len(mapp[0])

  for i in range(lines):
    for j in range(columns):
      if mapp[i][j] == symbol:
        return (i, j)

if __name__ == "__main__":
  print(solution())
