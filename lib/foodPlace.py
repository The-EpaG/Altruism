from lib.person import Person


class FoodPlace(object):
    def __init__(self, food: int) -> None:
        self.maxFood = food
        self.food = food
        self.people: list[Person] = []

    def isFull(self) -> bool:
        return len(self.people) == 2

    def addPerson(self, person: Person) -> bool:
        if self.isFull():
            return False
        self.people.append(person)
        return True

    def serveFood(self) -> None:
        if self.people == []:
            return

        if len(self.people) != 1:
            self.people[0].eat(self.food, self.people[1])
            self.people[1].eat(self.food, self.people[0])
        else:
            self.people[0].eat(self.food)

        self.food = 0
        self.people = []

    def nextDay(self) -> None:
        self.food = self.maxFood
