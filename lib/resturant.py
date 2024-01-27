from lib.foodPlace import FoodPlace
from lib.person import Person


class Resturant:
    def __init__(self, foodPlace: int) -> None:
        self.foodPlace:list[FoodPlace] = list(map(lambda _: FoodPlace(2), range(foodPlace)))
        self.freePlaces:list[FoodPlace] = self.foodPlace[:]

    def eat(self, person: Person) -> None:
        if self.freePlaces == []:
            return False

        foodPlace: FoodPlace = self.freePlaces[0]
        foodPlace.addPerson(person)
        if foodPlace.isFull():
            self.freePlaces = self.freePlaces[1:]
        return True

    def serveFood(self) -> None:
        for foodPlace in self.foodPlace:
            foodPlace.serveFood()

    def nextDay(self) -> None:
        for foodPlace in self.foodPlace:
            foodPlace.nextDay()