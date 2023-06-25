# Write your solution here:
from random import randint


def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        random_word = "".join(
            characters[randint(0, len(characters) - 1)] for i in range(length)
        )
        yield random_word
