class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return (
            f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
        )


def accepted(attemps: list):
    return list(filter(lambda attempt: attempt.grade >= 1, attemps))


def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda attempt: attempt.grade == grade, attempts))


def passed_students(attempts: list, course: str):
    return sorted(
        map(
            lambda x: x.student_name,
            list(
                filter(
                    lambda attempt: attempt.course_name == course and attempt.grade > 0,
                    attempts,
                )
            ),
        ),
    )
