# pylint: disable=bad-indentation

"""
Advent of Code Day 4 Part 2.
"""

RELATIVE_PATH = "../inputs/input.txt"
RELATIVE_PATH_TEST = "../inputs/short.txt"

def solution():
  """Solution"""

  letter_matrix = []

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      matrix_line = []
      for letter in line:
        if letter != '\n':
          matrix_line.append(letter)
      letter_matrix.append(matrix_line)

  xmas_sum = 0

  lines = len(letter_matrix)
  columns = len(letter_matrix[0])

  for i in range(lines - 2):
    for j in range(columns - 2):
        sub_matrix = [row[j:j+3] for row in letter_matrix[i:i+3]]

        xmas_sum += int(find_xmas(sub_matrix))

  return xmas_sum

def find_xmas(matrix):
  """Find X-MAS in 3*3 matrix"""

  target = ('MAS', 'SAM')

  diag = matrix[0][0] + matrix[1][1] + matrix[2][2]
  anti_diag = matrix[0][2] + matrix[1][1] + matrix[2][0]

  return diag in target and anti_diag in target

if __name__ == "__main__":
  print(solution())
