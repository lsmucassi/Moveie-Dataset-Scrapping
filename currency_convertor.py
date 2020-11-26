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

word_re = rf"\${number}(-|\sto\s)?({number})?\s({amount})"
value_re = rf"\${number}"

def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict[word]

def parse_word_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    word = re.search(amount, string, flags=re.I).group().lower()
    word_value = word_to_value(word)
    return value*word_value 

def parse_value_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    return value

def money_conversion(money):
    if isinstance(money, list):
        money= money[0]

    word_syntax = re.search(word_re, money, flags=re.I)
    value_syntax = re.search(value_re, money)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())
    elif value_syntax:
        return parse_value_syntax(value_syntax.group())


# print(re.search(word_re, "$12.2 million").group())
print(money_conversion("$12 Million"))


