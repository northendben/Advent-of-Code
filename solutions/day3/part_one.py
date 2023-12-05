import pdb
import re
import sys
sys.path.append('../../')
import input_parser

symbol_regex = re.compile(r"[^.a-zA-Z0-9]")
part_regex = re.compile(r"(\d+)")
puzzle_input = input_parser.input_parser('day3', 'input')
acceptable_values = [-1,0,1]
total = 0
top_limit = 0
bottom_limit = len(puzzle_input)
left_limit = 0
right_limit = len(puzzle_input[0])

for index,row in enumerate(puzzle_input):
    print(index)
    parts = list(re.finditer(part_regex, row))
    symbols_in_row = list(re.finditer(symbol_regex, row))
    for match in parts:
        part_location = match.span()
        part_range = range(part_location[0], part_location[1])
        for symbol in symbols_in_row: #check same row
            if any(symbol.span()[0] - num in acceptable_values for num in part_range):
                num_to_add = int(match.group())
                total += num_to_add
        #check above
        if index > top_limit:
            symbols_in_row_above = list(re.finditer(symbol_regex, puzzle_input[index-1]))
            for symbol in symbols_in_row_above:
                if any(symbol.span()[0] - num in acceptable_values for num in part_range):
                    num_to_add = int(match.group())
                    total += num_to_add
        if index < bottom_limit -1:
            symbols_in_row_below = list(re.finditer(symbol_regex, puzzle_input[index+1]))
            for symbol in symbols_in_row_below:
                if any(symbol.span()[0] - num in acceptable_values for num in part_range):
                    num_to_add = int(match.group())
                    total += num_to_add
        print(total)
print(total)


            


