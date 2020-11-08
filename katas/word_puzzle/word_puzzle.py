"""
http://codekata.com/kata/kata19-word-chains/
Write a program that solves word-chain puzzles.

There’s a type of puzzle where the challenge is to build a chain of words,
starting with one particular word and ending with another.
Successive entries in the chain must all be real words, and each can differ from the
previous word by just one letter.
For example, you can get from “cat” to “dog” using the following chain.

1 cat
2 cot
3 cog
4 dog

The objective of this kata is to write a program that accepts start and end words and,
using words from the dictionary, builds a word chain between them. For added programming fun,
return the shortest word chain that solves each puzzle.
For example, you can turn “lead” into “gold” in four steps (lead, load, goad, gold),
and “ruby” into “code” in six steps (ruby, rubs, robs, rods, rode, code).
"""


def get_next_letter(letter):
    if letter == 'z':
        return None
    return string.ascii_lowercase.split(letter)[1][0]


import string

start_word = input("Start word: ").strip().lower()
end_word = input("End word: ").strip().lower()

if len(start_word) == 0 or len(end_word) == 0:
    print("Passed words should be > 1 character length: ", start_word, end_word)
    exit(1)

if start_word > end_word:
    print("Start word should be after end word: ", start_word, end_word)
    exit(1)

if len(start_word) != len(end_word):
    print("Start word should be same character count as end word ", start_word, end_word)
    exit(1)

dictionary = set()
with open('wordlist.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for word in f:
        dictionary.add(word.strip().lower())

if start_word not in dictionary:
    print("Start word should be a valid word: ", start_word)
    exit(1)

if end_word not in dictionary:
    print("End word should be a valid word: ", start_word)
    exit(1)

next_word = start_word
word_chain = []

for i in reversed(range(len(start_word))):
    current_character = next_word[i]
    next_character = get_next_letter(current_character)

    # todo
    
    if next_word in dictionary:
        word_chain.append(next_word)

    if next_word == end_word:
        break
