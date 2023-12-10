import re
import sys
sys.path.append('../../')
import input_parser
split_regex = re.compile(r"(\D+\d+\: )|(\|)")
num_regex = re.compile(r'\d+')
puzzle_input = input_parser.input_parser('day4', 'input')
card_count_lookup = dict.fromkeys(range(1, len(puzzle_input) + 1), 1)

for index, row in enumerate(puzzle_input, start=1):
    times_to_loop = card_count_lookup[index]
    start_add_index = index + 1
    row = list(filter(None, re.split(split_regex, row )))
    game = row[0]
    winning_numbers = [int(num) for num in re.findall(num_regex, row[1])]
    winning_numbers.sort()
    elf_numbers = [int(num) for num in re.findall(num_regex, row[3])]
    elf_numbers.sort()
    while times_to_loop > 0:
        cards_to_copy = 0
        for num in winning_numbers:
            if num in elf_numbers:
                cards_to_copy += 1
        for num in range(start_add_index,start_add_index + cards_to_copy):
            card_count_lookup[num] += 1
        times_to_loop -= 1
            
print(card_count_lookup)
total = 0

for num in card_count_lookup.values():
    total += num
print(total)









