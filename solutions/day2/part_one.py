import pdb
import re
import sys
sys.path.append('../../')
import input_parser

input = input_parser.input_parser('day2')
blue_regex = re.compile(r"\d* blue")
red_regex = re.compile(r"\d* red")
green_regex = re.compile(r"\d* green")
score = 0

green_limit = 13
red_limit = 12
blue_limit = 14


for index, row in enumerate(input, start=1):
    if any([int(item.split(' ')[0]) > blue_limit for item in re.findall(blue_regex, row)]):
        continue
    elif any([int(item.split(' ')[0]) > red_limit for item in re.findall(red_regex, row)]):
        continue
    elif any([int(item.split(' ')[0]) > green_limit for item in re.findall(green_regex, row)]):
        continue
    else:
        score += index

print(score)
