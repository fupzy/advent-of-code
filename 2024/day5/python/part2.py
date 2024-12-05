# pylint: disable=bad-indentation

"""
Advent of Code Day 5 Part 2.
"""

from collections import defaultdict, deque

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

  invalid = invalid_updates(rules, updates)

  return compute_invalid_update_sum(correct_updates(rules, invalid))

def correct_updates(rules, updates):
  """Correct all invalid updates"""

  valid = []

  for update in updates:
    valid.append(correct_update(rules, update))

  return valid

def correct_update(rules, update):
  """Correct an invalid update into a valid one"""

  graph = defaultdict(list) # Dependencies graph/dict.
  in_degree = {x: 0 for x in update} # Incoming dependencies for each graph element.

  for a, b in rules:
      # For each rules, if a and b are parts of the update we add the dependency in the graph.
      if a in in_degree and b in in_degree:
          graph[a].append(b)
          in_degree[b] += 1

  # Independant elements of the update.
  queue = deque([node for node in update if in_degree[node] == 0])

  sorted_list = []
  while queue:
      node = queue.popleft()
      sorted_list.append(node)
      for neighbor in graph[node]:
          in_degree[neighbor] -= 1
          if in_degree[neighbor] == 0:
              queue.append(neighbor)

  return sorted_list

def compute_invalid_update_sum(invalid_updates_bis):
  """return the sum of the middle num of each valid updates"""

  invalid_update_sum = 0

  for update in invalid_updates_bis:
    update_size = len(update)

    invalid_update_sum += update[update_size // 2]

  return invalid_update_sum

def invalid_updates(rules, updates):
  """return all valid updates"""

  invalid_updates_list = []

  for update in updates:
    if check_update(rules, update):
      invalid_updates_list.append(update)

  return invalid_updates_list

def check_update(rules, update):
  """Tells wheter an update respect the rules or not"""

  update_size = len(update)

  for i in range(update_size):
    current_number = update[i]

    for j in range(i + 1, update_size):
      next_number = update[j]

      if not check_rules(rules, current_number, next_number):
        return True

  return False

def check_rules(rules, a, b):
  """Tells if the a,b sequence follows the rules or not"""

  for rule in rules:
    if rule[0] == b and rule[1] == a:
      return False

  return True

if __name__ == "__main__":
  print(solution())
