from turtle import Turtle
from random import randint
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.increase = 0

    def generate_car(self):
        choice_of_getting_five = random.randint(1, 6)
        if choice_of_getting_five == 5:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_point = randint(-240, 240)
            new_car.goto(280, y_point)
            self.all_cars.append(new_car)

    def move(self):
        count = 0
        for i in self.all_cars:
            count += 1
            print(f"count  is  {count}")
            i.backward(STARTING_MOVE_DISTANCE + self.increase * MOVE_INCREMENT)




