# Write your solution here
def copy_lines(source_file: str, target_file: str, criterion=lambda x: True):
    with open(source_file) as source, open(target_file, "w") as target:
        for line in source:
            # Remove any whitespace from beginning and end of line
            line = line.strip()

            if criterion(line):
                target.write(line + "\n")


def search(products: list, criterion: callable):
    return [product for product in products if criterion(product)]
