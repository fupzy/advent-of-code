#!/bin/bash

# Script to generate directories and files for Advent of Code Days 1 to 25.

BASE_DIR="../2024"

# Create the base directory if it doesn't exist
mkdir -p "$BASE_DIR"

cd $BASE_DIR

for i in $(seq 1 25)
do
    # Create the day{i} directory
    mkdir -p "day$i/inputs" "day$i/python"

    # Content for part1.py
    cat <<EOL > "day$i/python/part1.py"
# pylint: disable=bad-indentation

"""
Advent of Code Day $i Part 1.
"""

RELATIVE_PATH = "../inputs/input.txt"

def solution():
  """Solution"""

if __name__ == "__main__":
  print(solution())
EOL

    # Content for part2.py
    cat <<EOL > "day$i/python/part2.py"
# pylint: disable=bad-indentation

"""
Advent of Code Day $i Part 2.
"""

RELATIVE_PATH = "../inputs/input.txt"

def solution():
  """Solution"""

if __name__ == "__main__":
  print(solution())
EOL
done