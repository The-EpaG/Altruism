class Day:
    def __init__(self, people: int) -> None:
        self.people = {
            "Starting": people,
            "Ending": 0,
        }
        self.food = []

    def eat(self, food: int) -> None:
        self.food.append(food)

    def add_ending_people(self, people: int) -> None:
        self.people["Ending"] = people

    def to_json(self) -> str:
        return {
            "people": self.people,
            "food": self.food,
        }

    def __str__(self) -> str:
        return str(self.to_json())
