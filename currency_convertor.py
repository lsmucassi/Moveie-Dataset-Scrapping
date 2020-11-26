import re


'''
TODO
Given either a string or a list of strings as input, return
a number (int or float) which is equal to the monetary value
money_conversion("$12.2 million") --> 12200000
money_conversion("$790,000") --> 790000
use test_money_conversion.py to test your solution
'''
amount = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"

word_re = rf"\${number}\s({amount})"
value_re = rf"\${number}"

def parse_value_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    return value

def money_conversion(money):
    word_syntax = re.search(word_re, money)
    value_syntax = re.search(value_re, money)

    if word_syntax:
        print("WORD SYNTAX")
        print(word_syntax.group())
    elif value_syntax:
        print("WORD SYNTAX")
        print(value_syntax.group())

    # value = float(word_re, money)
    # return value


# print(re.search(word_re, "$12.2 million").group())
print(money_conversion("$12,20000 million"))


