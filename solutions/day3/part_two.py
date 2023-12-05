import pdb
import re
import sys
sys.path.append('../../')
import input_parser
import pdb

symbol_regex = re.compile(r"(\*)")
part_regex = re.compile(r"(\d+)")
puzzle_input = input_parser.input_parser('day3', 'comm_test')
acceptable_values = [-1,0,1]
total = 0
top_limit = 0
bottom_limit = len(puzzle_input)
left_limit = 0
right_limit = len(puzzle_input[0])
for index,row in enumerate(puzzle_input):
    # print(row)
    pdb.set_trace()
    num_of_parts_matched = 0
    final_parts_matched = []
    symbols_in_row = list(re.finditer(symbol_regex, row))
    parts_in_row = list(re.finditer(part_regex, row))
    for symbol in symbols_in_row:
        for part in parts_in_row:
            part_location = part.span()
            part_range = range(part_location[0], part_location[1])
            if any(symbol.span()[0] - num in acceptable_values for num in part_range):
                num_of_parts_matched += 1
                final_parts_matched.append(part.group())
        if index > top_limit:
            parts_in_row_above = list(re.finditer(part_regex, puzzle_input[index-1]))
            for part in parts_in_row_above:
                part_location = part.span()
                part_range = range(part_location[0], part_location[1])
                if any(symbol.span()[0] - num in acceptable_values for num in part_range):
                    num_of_parts_matched += 1
                    final_parts_matched.append(part.group())
        if index < bottom_limit -1:
            parts_in_row_below = list(re.finditer(part_regex, puzzle_input[index+1]))
            for part in parts_in_row_below:
                part_location = part.span()
                part_range = range(part_location[0], part_location[1])
                if any(symbol.span()[0] - num in acceptable_values for num in part_range):
                    num_of_parts_matched += 1
                    final_parts_matched.append(part.group())
    if num_of_parts_matched == 2:
        row_product = int(final_parts_matched[0]) * int(final_parts_matched[1])
        total += row_product
print(total)

        