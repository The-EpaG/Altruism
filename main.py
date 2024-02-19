import os
import json
import logging
import colorlog
from lib.constant import (
    LOG_LEVEL,
    LOG_FORMAT,
    MAX_DAY,
    OUTPUT_FILE,
    OUTPUT_FOLDER,
    SAVE,
    SHOW,
    FOOD_PLACE,
    POPULATION,
)

from lib.data import Data
from lib.day import Day
from lib.graph import Graph
from lib.world import World


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(LOG_FORMAT))
logging.basicConfig(level=LOG_LEVEL, handlers=[handler])
logger = logging.getLogger(__name__)

population: list[int] = []
food: list[int] = []
data: Data = Data()

world = World(FOOD_PLACE)
world.populate(POPULATION)

logger.info(f"Food place: {world.food_place}")
logger.info(f"People at the start: {world.population}")
logger.info(f"Day to simulate: {MAX_DAY}")

logger.info("Starting simulation...")

for day_number in range(MAX_DAY):
    logger.debug(f"Day {day_number}")
    # New day
    day = Day(world.population)

    # Eat
    world.eat()
    day.eat(world.remaining_food)
    food.append(world.remaining_food)
    population.append(world.nextDay())

    # Ending day
    day.add_ending_people(world.population)
    data.add_day(day_number, day)


logger.debug(data)
logger.info(f"Min food: {min(food)}")
logger.info(f"Max population: {max(population)}")

if SHOW:
    logger.info("Plotting...")

    graph = Graph()
    graph.plot_y(population, show=False, label="population")
    graph.plot_y(food, label="food")

    logger.info("Plotted")

if SAVE:
    logger.info(f"Saving data to {OUTPUT_FOLDER}/{OUTPUT_FILE}")

    if not os.path.exists(OUTPUT_FOLDER):
        logger.info(f"Creating {OUTPUT_FOLDER}")

        os.makedirs(OUTPUT_FOLDER)

    with open(f"{OUTPUT_FOLDER}/{OUTPUT_FILE}", "w") as f:
        f.write(json.dumps(data.to_json()))

    logger.info(f"Saved data to {OUTPUT_FOLDER}/{OUTPUT_FILE}")

logger.info("Done")
