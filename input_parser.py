def input_parser(day, file):
    with open(f'../../inputs/{day}/{file}.txt', 'r') as file:
        return [(row.replace('\n', '')) for row in file]