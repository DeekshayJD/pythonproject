import math
import os
import random
import re
import sys


def top_three_compny_character(company_name):
    char_count = {}
    for char in company_name:
        char_count[char] = char_count.get(char, 0) + 1
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_chars[:3]:
        print(char, count)


if __name__ == '__main__':
    s = input("enter company name :-")
    top_three_compny_character(s)