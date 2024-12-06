# pylint: disable=bad-indentation

"""
Advent of Code Day 6 Part 2.
"""

import copy

RELATIVE_PATH = "../inputs/input.txt"
RELATIVE_PATH_TEST = "../inputs/short.txt"
RELATIVE_PATH_TEST_CUSTOM = "../inputs/short_test.txt"

def solution():
  """Solution"""

  map_matrix = []

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      map_matrix.append(line[:-1] if line[-1] == '\n' else line)

  print("\n".join(map(str, map_matrix)))

  return find_all_cycles(map_matrix)

def get_init_pos(mapp, symbol):
  """Returns the beginning position"""

  lines = len(mapp)
  columns = len(mapp[0])

  for i in range(lines):
    for j in range(columns):
      if mapp[i][j] == symbol:
        return (i, j)

  return (-1, -1)

def is_cycle(path):
  """Check if there is a cycle"""

  path_size = len(path)

  if path_size < 6:
    return False

  last, before_last = path[-1], path[-2]
  for i in range(path_size - 3):
    if path[i] == before_last and path[i + 1] == last:
      return True

  return False

def find_all_cycles(mapp):
  """Compute all possibilities"""

  lines = len(mapp)
  columns = len(mapp[0])

  counter = 0

  for i in range(lines):
    for j in range(columns):
      print(f"{(i, j)} over {(lines, columns)}")
      if mapp[i][j] != '#' and mapp[i][j] != '^':
        new_map = copy.deepcopy(mapp)
        new_map[i] = new_map[i][:j] + '#' + new_map[i][j + 1:]

        counter += process_route(new_map)

  return counter

def process_route(mapp):
  """Process the route whithin the map"""

  init_dir = '^'
  init_x, init_y,  = get_init_pos(mapp, init_dir)

  visited_pos = [(init_x, init_y)]

  next_mov = next_move(init_x, init_y, init_dir, mapp)
  # print((init_x, init_y))

  while next_mov is not None:
    next_x, next_y, next_dir = next_mov
    # a = input()

    visited_pos.append((next_x, next_y))
    if is_cycle(visited_pos):
      return 1

    # print((next_x, next_y))

    next_mov = next_move(next_x, next_y, next_dir, mapp)

  return 0


def next_move(x, y, direction, mapp):
  """Compute next move in the map"""

  next_x, next_y = x, y
  next_dir = direction
  symbol_mapper = {
    '^' : '>',
    '>' : 'v',
    'v' : '<',
    '<' : '^'
  }

  match direction:
    case '^':
      next_x -= 1
    case '>':
      next_y += 1
    case 'v':
      next_x += 1
    case '<':
      next_y -= 1

  if not is_in_map(mapp, next_x, next_y):
    return None

  if mapp[next_x][next_y] == '#':
    next_dir = symbol_mapper[next_dir]

    return next_move(x, y, next_dir, mapp)

  return (next_x, next_y, next_dir)

def is_in_map(mapp, i, j):
  """Returns true if i and j are mapp indexes"""

  lines = len(mapp)
  columns = len(mapp[0])

  return i >= 0 and i < lines and j >= 0 and j < columns

if __name__ == "__main__":
  print(solution())
