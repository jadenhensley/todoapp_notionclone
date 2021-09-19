from random import randint
from random import choice
import pathlib
import time
import csv
import os

# cwd = os.getcwd()

# def replaceBackslashes(string):
#     print(string)
#     newstring=""
#     for char in string:
#         if char == "\\":
#             newstring += "/"
#         else:
#             newstring += char
#     print(newstring)

# propercwd = replaceBackslashes(cwd)

with open(f'media/QuotesForDevelopers.csv', 'r') as csv_quotes:
    csv_reader = csv.DictReader(csv_quotes, delimiter=";")
    quotes = []
    author = []
    for row in csv_reader:
        quotes.append(row['QUOTE'])
        author.append(row['AUTHOR'])
    
def getDailyQuote():
    indice = randint(0, len(quotes)-1)
    return '"   ' + quotes[indice] + '   "' + "\n\tquote from: " + author[indice] + "\n";
