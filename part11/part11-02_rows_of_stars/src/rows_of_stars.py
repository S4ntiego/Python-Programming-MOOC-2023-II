# WRITE YOUR SOLUTION HERE:
def rows_of_stars(numbers: list):
    return [num * "*" for num in numbers]


if __name__ == "__main__":
    rows = rows_of_stars([4, 3, 2, 1, 10])
    for row in rows:
        print(row)
