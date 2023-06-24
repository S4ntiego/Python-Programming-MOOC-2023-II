import string


# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    word_counts = {}
    with open(filename, "r") as file:
        for line in file:
            line.strip().lower()
            line = "".join(char for char in line if char not in string.punctuation)

            words = line.split()
            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1

    common_words = {
        word: count for word, count in word_counts.items() if count >= lower_limit
    }
    return common_words


if __name__ == "__main__":
    most_common_words("programming.txt", 3)
