import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import player

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
turtle_player = Player()
# listen up for user key
screen.listen()
screen.onkey(fun=turtle_player.user_input_up, key="Up")
screen.onkey(fun=turtle_player.user_input_down, key="Down")
car = CarManager()


score_keeper = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move()

    # Detect collision of the turtle with the car
    for single_car in car.all_cars:
        if single_car.distance(turtle_player) < 20:
            score_keeper.game_over()
            game_is_on = False

    # increase the level of the player
    if turtle_player.ycor() > player.FINISH_LINE_Y:
        turtle_player.create_player()
        score_keeper.increase_level()
        car.increase += 0.5

screen.exitonclick()