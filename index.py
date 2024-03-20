# Script to order an array of strings in json format by their length.
# Author: Pol Gubau Amores.
# Date: 2024/03/20

# Expected input: 
# {
#   "words": [    
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
    for word in strings["words"]:
        # Get the length of the string
        length = len(word)
        # If the length is not in the dictionary, create a new list
        if length not in ordered_strings:
            ordered_strings[length] = []
        # Add the string to the list
        ordered_strings[length].append(word)
    return ordered_strings





def main():

    # Read the json from 'input.json'
    data = json.load(sys.stdin)

    # Order the strings by their length
    ordered_strings = order_strings_by_length(data)

    # Create a 'output.json' file with the ordered strings
    with open("output.json", "w") as output_file:
        json.dump(ordered_strings, output_file)

    print("The strings have been ordered by their length in 'output.json'")
 


if __name__ == "__main__":
    main()

