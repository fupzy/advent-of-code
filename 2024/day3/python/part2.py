# pylint: disable=bad-indentation

"""
Advent of Code Day 3 Part 2.
"""

import re

RELATIVE_PATH = "../inputs/input.txt"

def solution():
  """Solution"""

  text = "do()"

  with open(RELATIVE_PATH, 'r', encoding='utf-8') as f:
    for line in f.readlines() :
      text += line


  mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
  all_products = []
  for match in re.finditer(mul_pattern, text):
      debut, fin = match.span()
      all_products.append({
          "expression": match.group(0),
          "indexes": (debut, fin)
      })

  products = authorized_products(authorized_indexes(text), all_products)

  return sum_products(products)

def authorized_products(authorized_slices, products):
  """Find all authorized products"""
  auth_producs = []

  for product in products:
      product_start, product_end = product['indexes']
      for slice_start, slice_end in authorized_slices:
          if slice_start <= product_start and product_end <= slice_end:
              auth_producs.append(product['expression'])
              break

  return auth_producs

def authorized_indexes(text):
    """Find all slices where mul are authorized"""

    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    do_positions = [match.end() for match in re.finditer(do_pattern, text)]
    dont_positions = [match.start() for match in re.finditer(dont_pattern, text)]

    slices = []
    for start in do_positions:
        for end in dont_positions:
            if start < end:
                slices.append((start, end))
                break
    print(slices)
    return slices



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
