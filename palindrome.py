#!/usr/bin/python

import argparse
import string
from collections import Counter


parser = argparse.ArgumentParser(description='Detect and output palindromes in files.')
parser.add_argument('input_file', type=argparse.FileType('r'))

def is_palindrome(word):
    if len(word) <= 1:
        return False

    # compare lowercase word with its reversed self
    return word.lower() == word[::-1].lower()

# split a line into words, removing punctuation
def parse_line(line):
    def strip_punctuation(word):
        return word.lower().strip(string.punctuation)

    # the outer 'list' is for python3 compatibility
    return list(filter(is_palindrome, map(strip_punctuation, line.split())))

# read from the file iterator per line(memory friendly!)
# parse each line and print every _new_ palindrome
# keep track of all seen ones and print the stats at the end
def print_palindromes(file_handle):
    seen_palindromes = Counter()

    for line in file_handle:
        for palindrome in parse_line(line):
            if not palindrome in seen_palindromes:
                print(palindrome)

            seen_palindromes[palindrome] += 1

    return seen_palindromes


if __name__ == "__main__":
    args = parser.parse_args()

    count = print_palindromes(args.input_file)

    if count:
        print("Found palindromes: {0}".format(count))
    else:
        print("No palindromes found in {0}".format(args.input_file.name))
