def input_parser(day):
    with open(f'../../inputs/{day}/input.txt', 'r') as file:
        return [(row.replace('\n', '')) for row in file]