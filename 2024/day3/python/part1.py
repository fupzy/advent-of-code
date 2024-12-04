# pylint: disable=bad-indentation

"""
Advent of Code Day 3 Part 1.
"""

import re

RELATIVE_PATH = "../inputs/input.txt"

def solution():
  """Solution"""

  pattern = r"mul\(\d{1,3},\d{1,3}\)"
  text = ""

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      text += line

  products = re.findall(pattern, text)

  return sum_products(products)

def sum_products(products: list):
  """Sum all matched products"""

  sum_prods = 0

  for product in products:
    sum_prods += compute_product(product)

  return sum_prods

def compute_product(product: str):
  """Convert a 'mul(a,b)' into its integer value"""

  a, b = product[4:-1].split(',')

  return int(a) * int(b)

if __name__ == "__main__":
  print(solution())
