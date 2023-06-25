# Write your solution here
def prime_numbers():
    x = 2
    while True:
        is_prime = True
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            yield x
        x += 1
