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

  lines = len(map_matrix)
  columns = len(map_matrix[0])

  counter = 0

  for i in range(lines):
    for j in range(columns):
      print(f"{(i, j)} over {(lines, columns)}")
      if map_matrix[i][j] != '#' and map_matrix[i][j] != '^':
        new_map = copy.deepcopy(map_matrix)
        new_map[i] = new_map[i][:j] + '#' + new_map[i][j + 1:]

        counter += process_route(new_map)

  return counter

def process_route(mapp):
  """Process the route whithin the map"""

  symbol_mapper = {
    '^' : '>',
    '>' : 'v',
    'v' : '<',
    '<' : '^'
  }

  current_dir = '^'
  current_x, current_y,  = get_init_pos(mapp, current_dir)

  visited_walls = []

  while True:

    match current_dir:
      case '^':
        current_x -= 1
      case '>':
        current_y += 1
      case 'v':
        current_x += 1
      case '<':
        current_y -= 1

    if not is_in_map(mapp, current_x, current_y):
      return 0

    if mapp[current_x][current_y] == '#':
      wall = (current_x, current_y, current_dir)
      if wall in visited_walls :
        return 1

      match current_dir:
        case '^':
          current_x += 1
        case '>':
          current_y -= 1
        case 'v':
          current_x -= 1
        case '<':
          current_y += 1

      visited_walls.append(wall)
      current_dir = symbol_mapper[current_dir]



def get_init_pos(mapp, symbol):
  """Returns the beginning position"""

  lines = len(mapp)
  columns = len(mapp[0])

  for i in range(lines):
    for j in range(columns):
      if mapp[i][j] == symbol:
        return (i, j)

  return (-1, -1)

def is_in_map(mapp, i, j):
  """Returns true if i and j are mapp indexes"""

  lines = len(mapp)
  columns = len(mapp[0])

  return i >= 0 and i < lines and j >= 0 and j < columns

if __name__ == "__main__":
  print(solution())
