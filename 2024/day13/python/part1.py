# pylint: disable=bad-indentation

"""
Advent of Code Day 13 Part 1.
"""

RELATIVE_PATH = "../inputs/input.txt"
RELATIVE_PATH_TEST = "../inputs/short.txt"

def solution():
  """Solution"""

  data = [[]]

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      if line == '\n':
        data[-1] = transform_data(data[-1])
        data.append([])
      else:
        data[-1].append(line.replace('\n', ''))
    data[-1] = transform_data(data[-1])

  return compute_all_costs(data)

def compute_all_costs(data: list[list]):
  """Sum all costs"""

  costs_sum = 0
  epoch = 0
  for level in data:
    epoch += 1
    print(f"{epoch}/{len(data)}")
    costs_sum += minimum_cost(level[2], level[0], level[1])

  return costs_sum

def minimum_cost(
      final_pos: tuple[int, int],
      button_1: tuple[int, int, int],
      button_2: tuple[int, int, int]
    ):
  """Finds the minimal cost to reach ()."""

  cost_1, x_mov_1, y_mov_1 = button_1
  cost_2, x_mov_2, y_mov_2 = button_2

  queue = [(0, 0, 0)]

  visited = {}

  while queue:
    queue.sort()
    current_cost, x, y = queue.pop(0)

    if x == final_pos[0] and y == final_pos[1]:
      return current_cost

    if (x, y) in visited and visited[(x, y)] <= current_cost:
      continue

    visited[(x, y)] = current_cost

    new_cost_1, new_x_1, new_y_1 = current_cost + cost_1, x + x_mov_1, y + y_mov_1
    new_cost_2, new_x_2, new_y_2 = current_cost + cost_2, x + x_mov_2, y + y_mov_2

    if new_x_1 <= final_pos[0] and new_y_1 <= final_pos[1]:
      queue.append((new_cost_1, new_x_1, new_y_1))
    if new_x_2 <= final_pos[0] and new_y_2 <= final_pos[1]:
      queue.append((new_cost_2, new_x_2, new_y_2))

  return 0


def transform_data(data: list[str]):
  """Parse data"""

  button_a = parse_button_line(data[0])
  button_b = parse_button_line(data[1])
  prize = parse_button_line(data[2])

  return [button_a, button_b, prize]

def parse_button_line(line: str):
  """Parse a line that describes a button"""

  is_b_in_line = (1 if 'B' in line else None)
  button_cost = 3 if 'A' in line else is_b_in_line

  coords = line.split(':')[1][1:].split(',')
  x_offset, y_offset = int(coords[0][2:]), int(coords[1][3:])

  if button_cost:
    return (button_cost, x_offset, y_offset)

  return (x_offset, y_offset)


if __name__ == "__main__":
  print(solution())
