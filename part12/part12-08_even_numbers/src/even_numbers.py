# Write your solution here
def even_numbers(beginning: int, maximum: int):
    for i in range(beginning, maximum + 1):
        if i % 2 == 0:
            yield i
