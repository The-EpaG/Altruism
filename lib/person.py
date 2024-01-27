from __future__ import annotations
import logging

from lib.object import Object

logger = logging.getLogger(__name__)


class Person(Object):
    class STATUS:
        ALIVE = "alive"
        DEAD = "dead"
        REPRODUCING = "reproducing"

    def __init__(self) -> None:
        super().__init__()
        self.food: float = 0

        logger.debug(f"Created person {self.id}")

    def eat(self, totalFood: float, opponent: Person = None) -> None:
        logger.debug(f"Person {self.id} is eating {totalFood} food")
        if opponent is None:
            logger.debug(f"Person {self.id} has no opponent")
            self.food += totalFood
        else:
            logger.debug(f"Person {self.id} has an opponent: {opponent.id}")
            self.food += totalFood / 2

    def passDay(self) -> Person | None:
        logger.debug(f"Person {self.id} is passing a day")

        food = self.food
        self.food = 0
        if food > 1:
            logger.debug(f"Person {self.id} is reproducing")
            return self.STATUS.REPRODUCING

        if food == 0:
            logger.debug(f"Person {self.id} is dead")
            return self.STATUS.DEAD

        logger.debug(f"Person {self.id} is alive")
        return self.STATUS.ALIVE
