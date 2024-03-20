# Script to order an array of strings in json format by their length.
# Author: Pol Gubau Amores.
# Date: 2024/03/20

# Expected input: 
# {
#  [
#    "string1",
#    "string2",
#    "string3",
#    ...
#  ]
# }

# Expected output:
# {
#  1: [
#    "s",
#    "s",
#    "s",
#    ...
#  ],
#  2: [
#    "ss",
#    "ss",
#    "ss",
#    ...
#  ],
#  3: [
#    "sss",
#    "sss",
#    "sss",
#    ...
#  ],
#  ...
# }

# Instructions:
# To run this script, execute the following command:
# python index.py < input.json
# where input.json is a json file with the input data.

 

import json
import sys

def order_strings_by_length(strings):
    # Create a dictionary to store the strings ordered by their length
    ordered_strings = {}
    for string in strings:
        length = len(string)
        if length in ordered_strings:
            ordered_strings[length].append(string)
        else:
            ordered_strings[length] = [string]
    return ordered_strings

def main():

    # Read input from stdin
    input_data = sys.stdin.read()
    input_json = json.loads(input_data)

    # Order the strings by their length
    ordered_strings = order_strings_by_length(input_json)

    # Print the ordered strings in json format
    print(json.dumps(ordered_strings, indent=2))

if __name__ == "__main__":
    main()

