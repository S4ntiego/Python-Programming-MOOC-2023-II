# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    means = []
    mean_person1 = (
        person1,
        (person1["result1"] + person1["result2"] + person1["result3"] / 3),
    )
    mean_person2 = (
        person2,
        (person2["result1"] + person2["result2"] + person2["result3"] / 3),
    )
    mean_person3 = (
        person3,
        (person3["result1"] + person3["result2"] + person3["result3"] / 3),
    )
    means.append(mean_person1)
    means.append(mean_person2)
    means.append(mean_person3)
    smallest = means[0]
    for person in means:
        if (person[1]) < smallest[1]:
            smallest = person
    return smallest[0]


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    smallest_average(person1, person2, person3)
