class Id:
    def __init__(self):
        self.current_id = 0

    def generate_id(self):
        self.current_id += 1
        return self.current_id


# Write your solution here:
class Task:
    def __init__(
        self,
        description: str,
        programmer: str,
        workload: int,
        id_generator: Id = Id(),
        finished: str = "NOT FINISHED",
    ):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = finished
        self.id_generator = id_generator
        self.id = self.id_generator.generate_id()

    def mark_finished(self):
        self.finished = "FINISHED"

    def is_finished(self):
        if self.finished == "FINISHED":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}"


class OrderBook:
    def __init__(self):
        self.tasks = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return list(set([task.programmer for task in self.tasks]))

    def mark_finished(self, id: int):
        if id not in [task.id for task in self.tasks]:
            raise ValueError(f"Order with id {id} not found")
        else:
            for task in self.tasks:
                if task.id == id:
                    task.mark_finished()

    def finished_orders(self):
        return [task for task in self.tasks if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.tasks if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer not found")
        else:
            return (
                len(
                    [
                        task
                        for task in self.tasks
                        if task.programmer == programmer and task.is_finished()
                    ]
                ),
                len(
                    [
                        task
                        for task in self.tasks
                        if task.programmer == programmer and not task.is_finished()
                    ]
                ),
                sum(
                    [
                        task.workload
                        for task in self.tasks
                        if task.programmer == programmer and task.is_finished()
                    ]
                ),
                sum(
                    [
                        task.workload
                        for task in self.tasks
                        if task.programmer == programmer and not task.is_finished()
                    ]
                ),
            )
