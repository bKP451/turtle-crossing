# turtle-crossing
## I have created the  working model of turtle-crossing  using turtle graphics of python.

![turtle-crossing](https://user-images.githubusercontent.com/97843847/161124266-fe00b222-2562-4a47-8fc4-d5dabf74b3ff.png)


I have made three classes :
- car_manager.py
- player.py 
- scoreboard.py

I have broke down the problem into these steps:
1. First of all, I have setup my turtle screen. I have setup the screen of width= 600 and height= 600. Then I have called screen.tracer(0) to disable animation.  Here screen = Screeen().
2.Then I have created turtle object. Player controls this turtle object with the up and down keys.
3. Now cars get randomly created at the right most part of the screen Here cars get created at 1/3 of the  screen update.
4. Then car gets moved by a certain distance. It moves along the negative x-axis. Its y-coordinate remains constant. 
5. After that, scoreboard telling information regarding the status of the  level is displayed.
6. When user reaches the uppermost part of the screen, the user's turtle gets positioned along the initial position and  the  level gets increased.
7. When the turtle collides with the car, the game ends and user gets shown the "GAME OVER".








Developed under the guidance of Angela Yu.
