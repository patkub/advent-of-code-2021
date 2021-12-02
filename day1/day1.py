#!/usr/bin/env python3

import sys

def count_increased(f):
  # how many measurements increased
  increased = 0
  # read first line
  previous = int(f.readline().strip())
  # read the rest of the file line-by-line
  for line in f:
    current = int(line.strip())
    if current > previous:
      increased += 1
    previous = current
  return increased

# parse arguments
if len(sys.argv) < 1:
  print("Usage: ./day1.py input")
  exit(1)

input_file = sys.argv[1]
with open(input_file) as f:
  increased = count_increased(f)
  print(increased)

