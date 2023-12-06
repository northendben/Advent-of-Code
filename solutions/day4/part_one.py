import re
import sys
sys.path.append('../../')
import input_parser
points = 0
split_regex = re.compile(r"(\D+\d+\: )|(\|)")
num_regex = re.compile(r'\d+')

puzzle_input = input_parser.input_parser('day4', 'input')
for row in puzzle_input:
    row = list(filter(None, re.split(split_regex, row )))
    game = row[0]
    winning_numbers = [int(num) for num in re.findall(num_regex, row[1])]
    winning_numbers.sort()
    elf_numbers = [int(num) for num in re.findall(num_regex, row[3])]
    elf_numbers.sort()
    row_points = 0
    for num in winning_numbers:
        if num in elf_numbers:
            if row_points > 0:
                row_points = row_points * 2
            else:
                row_points = 1
    points += row_points
print(points)






