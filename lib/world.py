from lib.person import Person
from lib.resturant import Resturant


class World:
    def __init__(self, foodPlace: int) -> None:
        self.resturant = Resturant(foodPlace)
        self.people: list[Person] = []

    def populate(self, population: int) -> None:
        for _ in range(population):
            self.people.append(Person())

    def eat(self) -> None:
        for person in self.people:
            if not self.resturant.eat(person):
                break
        self.resturant.serveFood()

    def nextDay(self) -> int:
        children: list[Person] = []
        deads: list[Person] = []

        for person in self.people:
            match person.passDay():
                case Person.STATUS.ALIVE:
                    pass
                case Person.STATUS.REPRODUCING:
                    children.append(Person())
                case Person.STATUS.DEAD:
                    deads.append(person)

        for dead in deads:
            self.people.remove(dead)

        self.people += children

        self.resturant.nextDay()

        return len(self.people)

    @property
    def remaining_food(self) -> int:
        return sum(map(lambda foodPlace: foodPlace.food, self.resturant.foodPlace))
