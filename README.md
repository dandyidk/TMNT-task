## To run the game

One terminal runs
```
$ roscore
```
Another runs
```
$ rosrun turtlesim turtlesim_node
```
and another runs the following script (from the catkin_ws directory)
```
./setup.sh
```
if you want to add in/take control of a turtle do (without the ""):
```
$ ./new_turtle.sh "TURTLE NAME"
```
if u want to start game (must be after spawning in all the turtles otherwise errors going to occur):
```
$ ./startgame.sh
```
## How to navigate the folders
#### turtle movement and turtle tracker
the turtle movement and tracker source codes are in the src scripts directory named turtle_movement.py
the turtle movement takes the input of the user and controls the turtle while the tracker tracks positions, health and attacks
#### Bash scripts
running new_turtle.sh creates a new turtle, setup.sh allows control of the turtle thats spawned in at the start of the game, and startgame.sh starts the tracker script
each of this scripts with the exception of startgame.sh adds in the name of the turtle to the text file located in the text directory
the text file is used to hold all turtles so that the tracker script can track them all, hence all turtles must spawn in first as the startgame.sh takes all the turtles names as arguments
the script that adds in the name of each turtle is located in the scripts directory

