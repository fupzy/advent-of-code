# pylint: disable=bad-indentation

"""
Advent of Code Day 1 Part 1.
"""

RELATIVE_PATH = "../inputs/input.txt"

def solution():
  """Solution"""

  left_list = []
  right_list = []

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      split_line = line.split(' ')

      left_list.append(int(split_line[0]))
      right_list.append(int(split_line[-1]))

  left_list.sort()
  right_list.sort()

  return sum_distances(left_list, right_list)

def sum_distances(list1: list, list2: list) :
  """Sum the distances between each element of list1 and list2"""

  distances_sum = 0

  size = len(list1)
  for index in range(size) :
    distances_sum += abs(list1[index] - list2[index])

  return distances_sum

if __name__ == "__main__":
  print(solution())
