# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
    if len(numbers) % 5 != 0:
        last_num_sum = numbers[-1] + 1
        numbers.append(last_num_sum)
        add_numbers_to_list(numbers)
