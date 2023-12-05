##lines of text first digit and lazst digit to form a two digit number
##use a regex to find first digit and last digit


##regex for first num: ^[\D]*(\d)
##regex for last num: [/.]*(\d)[a-zA-Z]*$

import re
import sys
sys.path.append('../../')
import input_parser

first_num_regex = re.compile(r"^[\D]*(\d)", re.IGNORECASE )
last_num_regex = re.compile(r"[/.]*(\d)[a-zA-Z]*$", re.IGNORECASE)
running_total = 0
input = input_parser.input_parser('day1')

for row in input:
    first_num = re.search(first_num_regex, row).groups()[0]
    last_num = re.search(last_num_regex, row).groups()[0]
    num_val = int(first_num + last_num)
    running_total += num_val

print(running_total)
    


 