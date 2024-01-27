import os
# import json

from lib.data import Data
from lib.day import Day
from lib.graph import Graph
from lib.world import World

MAX_DAY = 40

OUTPUT_FOLDER = "output"
OUTPUT_FILE = "output.json"

population: list[int] = []
food: list[int] = []
data: Data = Data()

world = World(10)
world.populate(1)

for day_number in range(MAX_DAY):
    # New day
    day = Day(len(world.people))

    # Eat
    world.eat()
    day.eat(world.remaining_food)
    food.append(world.remaining_food)
    population.append(world.nextDay())

    # Ending day
    day.add_ending_people(len(world.people))
    print(day)
    data.add_day(day_number, day)

print(f"Min food: {min(food)}")
print(f"Max population: {max(population)}")

graph = Graph()
graph.plot_y(population, show=False, label="population")
graph.plot_y(food, label="food")

# if not os.path.exists(OUTPUT_FOLDER):
#     os.makedirs(OUTPUT_FOLDER)
# with open(f"{OUTPUT_FOLDER}/{OUTPUT_FILE}", "w") as f:
#     f.write(json.dumps(data.to_json()))
