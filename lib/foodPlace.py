import logging

from lib.object import Object
from lib.person import Person

logger = logging.getLogger(__name__)


class FoodPlace(Object):
    def __init__(self, food: int) -> None:
        super().__init__()

        self.maxFood = food
        self.food = food
        self.people: list[Person] = []

        logger.debug(f"Created food place {self.id} with food: {food}")

    def isFull(self) -> bool:
        return len(self.people) == 2

    def addPerson(self, person: Person) -> bool:
        logger.debug(f"Trying to add person {person.id} to food place {self.id}")

        if self.isFull():
            logger.debug(f"Food place {self.id} is full")
            return False

        self.people.append(person)
        logger.debug(f"Added person {person.id} to food place {self.id}")
        return True

    def serveFood(self) -> None:
        logger.debug(f"Serving food from food place {self.id}")
        if self.people == []:
            logger.debug(f"Food place {self.id} is empty")
            return

        if len(self.people) != 1:
            logger.debug(f"Food place {self.id} has multiple people")
            self.people[0].eat(self.food, self.people[1])
            self.people[1].eat(self.food, self.people[0])
        else:
            logger.debug(f"Food place {self.id} has one person")
            self.people[0].eat(self.food)

        self.food = 0
        self.people = []

        logger.debug(f"Served food from food place {self.id}")

    def nextDay(self) -> None:
        logger.debug(f"Next day in food place {self.id}")

        self.food = self.maxFood

    def hasAllFood(self) -> bool:
        return self.food == self.maxFood and len(self.people) == 0
