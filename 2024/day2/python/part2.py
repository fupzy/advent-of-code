# pylint: disable=bad-indentation

"""
Advent of Code Day 2 Part 2.
"""

RELATIVE_PATH = "../inputs/input.txt"

def solution():
  """Solution"""

  safe_reports_count = 0

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      levels = list(map(int, line.split(' ')))

      safe_reports_count += int(is_report_safe_with_one_error(levels))

  return safe_reports_count

def is_report_safe_with_one_error(levels: list):
  """Tells whether a report is safe with a one error tolerence"""

  report_size = len(levels)

  for index in range(report_size) :
    levels_with_one_error = levels[:index] + levels[index + 1:]

    if is_report_safe(levels_with_one_error) :
      return True

  return False

def is_report_safe(levels: list):
  """Tells whether a report is safe or note according to the rules"""

  is_ascending, is_descending = True, True
  report_size = len(levels)

  if report_size > 1 :
    previous_level = levels[0]
    for index in range(1, report_size):
      current_level = levels[index]

      if check_asc(current_level, previous_level) :
        is_ascending = False

      if check_desc(current_level, previous_level) :
        is_descending = False

      if not is_ascending and not is_descending:
        return False

      previous_level = current_level

  return is_ascending or is_descending

def check_asc(level_a, level_b):
  """check is level_a and level_b follows the ascending rule"""

  return level_a <= level_b or level_a - level_b > 3

def check_desc(level_a, level_b):
  """check is level_a and level_b follows the descending rule"""

  return level_a >= level_b or level_b - level_a > 3


if __name__ == "__main__":
  print(solution())
