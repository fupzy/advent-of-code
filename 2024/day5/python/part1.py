# pylint: disable=bad-indentation

"""
Advent of Code Day 5 Part 1.
"""

RELATIVE_PATH = "../inputs/input.txt"
RELATIVE_PATH_TEST = "../inputs/short.txt"

def solution():
  """Solution"""

  rules = []
  updates = []
  part_1_separator = '|'
  part_2_separator = ','

  is_parsing_part_1 = True
  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      if line == "\n":
        is_parsing_part_1 = False
        continue

      if is_parsing_part_1 :
        n1, n2 = line[:-1].split(part_1_separator)

        rules.append((int(n1), int(n2)))

      else :
        newline = line
        if line[-1] == '\n':
          newline = line[:-1]
        mapped_numbers = map(int, newline.split(part_2_separator))

        updates.append(list(mapped_numbers))

  return compute_valid_update_sum(valid_updates(rules, updates))

def compute_valid_update_sum(valid_updates_bis):
  """return the sum of the middle num of each valid updates"""

  valid_update_sum = 0

  for update in valid_updates_bis:
    update_size = len(update)

    valid_update_sum += update[update_size // 2]

  return valid_update_sum

def valid_updates(rules, updates):
  """return all valid updates"""

  valid_updates_list = []

  for update in updates:
    if check_update(rules, update):
      valid_updates_list.append(update)

  return valid_updates_list

def check_update(rules, update):
  """Tells wheter an update respect the rules or not"""

  update_size = len(update)

  for i in range(update_size):
    current_number = update[i]

    for j in range(i + 1, update_size):
      next_number = update[j]

      if not check_rules(rules, current_number, next_number):
        return False

  return True

def check_rules(rules, a, b):
  """Tells if the a,b sequence follows the rules or not"""

  for rule in rules:
    if rule[0] == b and rule[1] == a:
      return False

  return True

if __name__ == "__main__":
  print(solution())
