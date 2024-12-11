# pylint: disable=bad-indentation

"""
Advent of Code Day 10 Part 2.
"""

RELATIVE_PATH = "../inputs/input.txt"
RELATIVE_PATH_TEST = "../inputs/short.txt"
RELATIVE_PATH_TEST_BIS = "../inputs/test1.txt"

def solution():
  """Solution"""

  map_matrix = []

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      matrix_line = []
      for element in line.replace('\n', ''):
        matrix_line.append(Node(int(element)))
      map_matrix.append(matrix_line)

  generate_graph(map_matrix)

  return count_trails_map(map_matrix)

class Node:
  """Node"""

  def __init__(self, value, neighbours = None):
    self.value = value
    self.neighbours = neighbours if neighbours is not None else []

  def __str__(self):
    return  f"{self.value} : neighbours = {[node.value for node in self.neighbours]}"

def count_trails_map(mapp: list[list[Node]]):
  """Sum all map trails"""

  sum_trails = 0
  lines = len(mapp)
  columns = len(mapp[0])

  for i in range(lines):
    for j in range(columns):
      sum_trails += count_trails(mapp[i][j])

  return sum_trails

def count_trails(start: Node):
  """Count trails from Node start"""

  trails_sum = 0

  if start.value != 0:
    return trails_sum

  to_check = [node for node in start.neighbours if node.value - start.value == 1]

  while len(to_check) > 0:
    # for ele in to_check:
    #   print(ele)

    # print()

    # input()

    current_node = to_check[0]

    if current_node.value == 9:
      trails_sum += 1

    to_check.remove(current_node)

    to_check += [node for node in current_node.neighbours if node.value - current_node.value == 1]

  return trails_sum

def generate_graph(mapp: list[list[Node]]):
  """Link the Nodes"""

  lines = len(mapp)
  columns = len(mapp[0])

  for i in range(lines):
    for j in range(columns):
      current_node = mapp[i][j]

      if i - 1 >= 0 and mapp[i - 1][j].value - current_node.value == 1:
        current_node.neighbours.append(mapp[i - 1][j])

      if i + 1 < lines and mapp[i + 1][j].value - current_node.value == 1:
        current_node.neighbours.append(mapp[i + 1][j])

      if j - 1 >= 0 and mapp[i][j - 1].value - current_node.value == 1:
        current_node.neighbours.append(mapp[i][j - 1])

      if j + 1 < columns and mapp[i][j + 1].value - current_node.value == 1:
        current_node.neighbours.append(mapp[i][j + 1])


if __name__ == "__main__":
  print(solution())
