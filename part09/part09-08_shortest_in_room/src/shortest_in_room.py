# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        return len(self.people) == 0

    def print_contents(self):
        for person in self.people:
            print(person)

    def shortest(self):
        if self.is_empty():
            return None
        shortest = self.people[0]
        for person in self.people:
            if person.height < shortest.height:
                shortest = person
        return shortest

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest = self.shortest()
        self.people.remove(shortest)
        return shortest
