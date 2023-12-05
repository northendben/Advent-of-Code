import pdb
import re
import sys
sys.path.append('../../')
import input_parser
# import pdb
input = input_parser.input_parser('day2')
blue_regex = re.compile(r"\d* blue")
red_regex = re.compile(r"\d* red")
green_regex = re.compile(r"\d* green")
score = 0

green_limit = 13
red_limit = 12
blue_limit = 14

for index, row in enumerate(input, start=1):
    # pdb.set_trace()
    min_blues = max([int(item.split(' ')[0]) for item in re.findall(blue_regex, row)])
    min_reds = max([int(item.split(' ')[0]) for item in re.findall(red_regex, row)])
    min_greens = max([int(item.split(' ')[0]) for item in re.findall(green_regex, row)])
    row_product = min_blues * min_reds * min_greens
    score += row_product

print(score)