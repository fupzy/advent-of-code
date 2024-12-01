# pylint: disable=bad-indentation

"""
Advent of Code Day 1 Part 2.
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

  return sum_similarities(left_list, right_list)

def sum_similarities(list1: list, list2: list) :
  """Sum the similarities"""

  similarities_sum = 0

  for element in list1 :
    similarities_sum += element * list2.count(element)

  return similarities_sum

if __name__ == "__main__":
  print(solution())
