# pylint: disable=bad-indentation

"""
Advent of Code Day 4 Part 1.
"""

from collections import defaultdict

RELATIVE_PATH = "../inputs/input.txt"
TEST = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

def solution():
  """Solution"""

  letter_matrix = [[]]

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      matrix_line = []
      for letter in line:
        if letter != '\n':
          matrix_line.append(letter)
      letter_matrix.append(matrix_line)

  columns = groups(letter_matrix, lambda x, y: x)
  columns = [''.join(col) for col in columns]

  rows = groups(letter_matrix, lambda x, y: y)
  rows = [''.join(row) for row in rows]

  diagonals = groups(letter_matrix, lambda x, y: x + y)
  diagonals = [''.join(diag) for diag in diagonals]

  anti_diagonals = groups(letter_matrix, lambda x, y: x - y)
  anti_diagonals = [''.join(anti_diag) for anti_diag in anti_diagonals]

  return find_all_xmas(columns) + find_all_xmas(rows) + find_all_xmas(diagonals) + find_all_xmas(anti_diagonals)

def find_all_xmas(lists):
  """Find XMAS and SAMX in all lists of lists"""

  xmas_sum = 0

  for list in lists:
    xmas_sum += find_xmas(list)

  return xmas_sum

def find_xmas(list: list):
  """Find XMAS and SAMX in the list"""

  return list.count('XMAS') + list.count('SAMX')

def groups(data, func):
  """Grouping"""

  grouping = defaultdict(list)
  for y in range(len(data)):
    for x in range(len(data[y])):
      grouping[func(x, y)].append(data[y][x])

  return list(map(grouping.get, sorted(grouping)))


if __name__ == "__main__":
  print(solution())
