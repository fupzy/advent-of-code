# pylint: disable=bad-indentation

"""
Advent of Code Day 2 Part 1.
"""

RELATIVE_PATH = "../inputs/input.txt"

def solution():
  """Solution"""

  safe_reports_count = 0

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      levels = list(map(int, line.split(' ')))

      safe_reports_count += int(is_report_safe(levels))

  return safe_reports_count

def is_report_safe(levels: list):
  """Tells whether a report is safe or note according to the rules"""

  is_ascending = True
  is_descending = True

  report_size = len(levels)

  if report_size > 1 :
    previous_level = levels[0]
    for index in range(1, report_size):
      current_level = levels[index]
      if (current_level >= previous_level or previous_level - current_level > 3) :
        is_descending = False
      if (current_level <= previous_level or current_level - previous_level > 3) :
        is_ascending = False

      previous_level = current_level

  return is_ascending or is_descending



if __name__ == "__main__":
  print(solution())
