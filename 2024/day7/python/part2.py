# pylint: disable=bad-indentation

"""
Advent of Code Day 7 Part 2.
"""

RELATIVE_PATH = "../inputs/input.txt"
RELATIVE_PATH_TEST = "../inputs/short.txt"

def solution():
  """Solution"""

  inputs = []

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      first_split = line.split(':')
      test_result = int(first_split[0])
      numbers = list(map(int, first_split[1][1:].split(' ')))

      inputs.append((test_result, numbers))

  # print(inputs)

  sum_results = 0

  for line in inputs:
    sum_results += try_calculation(line[0], line[1])

  return sum_results

def try_calculation(expected_result, numbers):
  """Tells if calculation with the numbers can match the result"""

  numbers_size = len(numbers)
  results_tree = [numbers[0]]

  for i in range(1, numbers_size):
    new_tree = []
    current_number = numbers[i]
    for result in results_tree:
      new_tree.append(result + current_number)
      new_tree.append(result * current_number)
      new_tree.append(int(f"{result}{current_number}"))

    results_tree = new_tree

  # print(results_tree)

  for result in results_tree:
    if result == expected_result:
      return result

  return 0

if __name__ == "__main__":
  print(solution())
