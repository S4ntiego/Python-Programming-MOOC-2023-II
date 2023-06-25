class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


def by_length(route: ClimbingRoute):
    return route.length


def by_difficulty(route: ClimbingRoute):
    return [route.grade, route.length]


# Write your solution herer:
def sort_by_length(routes: list):
    return sorted(routes, key=by_length, reverse=True)


def sort_by_difficulty(routes: list):
    return sorted(routes, key=by_difficulty, reverse=True)
