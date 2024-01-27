from lib.day import Day


class Data:
    def __init__(self):
        self.data: dict[int, Day] = {}

    def add_day(self, index: int, day: Day) -> None:
        self.data[index] = day

    def __str__(self) -> str:
        return str(self.to_json())

    def to_json(self) -> list:
        return [day.to_json() for day in self.data.values()]
