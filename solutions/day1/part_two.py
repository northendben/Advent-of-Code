import re
import sys
sys.path.append('../../')
import input_parser
import pdb


running_total = 0

num_lookup = {
    "one": "on1e",
    "two": "tw2o",
    "three": "thre3e",
    "four": "fou4r",
    "five": "fiv5e",
    "six": "si6x",
    "seven": "seve7n",
    "eight": "eigh8t",
    "nine": "nin9e",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8", 
    "9": "9"
}

input = input_parser.input_parser('day1')
first_num_regex = re.compile(r"(?<!one|two|six)(?<!three|seven|eight)(?<!four|five|nine)(?<!\d)(one|two|three|four|five|six|seven|eight|nine|\d)", re.IGNORECASE)
# last_num_regex = re.compile(r"(?:(one|two|three|four|five|six|seven|eight|nine))*(?<=.)(?=\D*$)|(\d)(?!.*one|.*two|.*three|.*four|.*five|.*six|.*seven|.*eight|.*nine|\d)")
last_num_regex = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|\d)(?!.*one|.*two|.*three|.*four|.*five|.*six|.*seven|.*eight|.*nine|.*\d)")
for row in input:
    for k,v in num_lookup.items():
        row = row.replace(k,v)
    print(row)
    first_num = num_lookup[re.search(first_num_regex, row).groups()[0]]
    last_num = num_lookup[re.search(last_num_regex, row).group()]
    num_val = int(first_num + last_num)
    running_total += num_val
    print(row, num_val, running_total)

print(running_total)