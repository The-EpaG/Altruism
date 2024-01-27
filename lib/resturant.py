import logging

from lib.foodPlace import FoodPlace
from lib.person import Person

logger = logging.getLogger(__name__)


class Resturant:
    def __init__(self, foodPlace: int) -> None:
        self.foodPlace: list[FoodPlace] = list(
            map(lambda _: FoodPlace(2), range(foodPlace))
        )
        self.freePlaces: list[FoodPlace] = self.foodPlace[:]

    def eat(self, person: Person) -> None:
        logger.debug(f"Person {person.id} is trying to eating")

        if self.freePlaces == []:
            logger.debug(f"Resturant is full")
            return False

        foodPlace: FoodPlace = self._choseFoodPlace()
        foodPlace.addPerson(person)
        logger.debug(f"Person {person.id} is eating in food place {foodPlace.id}")

        if foodPlace.isFull():
            logger.debug(f"Food place {foodPlace.id} is full")
            self.freePlaces = self.freePlaces[1:]
        return True

    def serveFood(self) -> None:
        logger.debug("Serving food")
        for foodPlace in self.foodPlace:
            foodPlace.serveFood()

    def nextDay(self) -> None:
        logger.debug("Next day")
        for foodPlace in self.foodPlace:
            foodPlace.nextDay()

        self.freePlaces = self.foodPlace[:]

    def _choseFoodPlace(self) -> FoodPlace:
        full_food = list(
            filter(lambda foodPlace: foodPlace.hasAllFood(), self.freePlaces)
        )
        if full_food:
            return full_food[0]
        return self.freePlaces[0]
