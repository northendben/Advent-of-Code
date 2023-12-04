import re

def find_one_or_two_no_spaces(input_string):
    # Construct a regex pattern to find the words "one" or "two" without spaces
    regex_pattern = r'\b(?:one|two)\b'
    
    # Use the regex pattern to find matches
    matches = re.findall(regex_pattern, input_string)

    if matches:
        print("Matches found:", ', '.join(matches))
    else:
        print("No matches found in the string.")

# Test with an example
input_string = "Thisisoneexamplewithtwowords."
find_one_or_two_no_spaces(input_string)