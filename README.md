## To run the game

One terminal runs
```
Roscore
```
Another runs
```
rosrun turtlesim turtlesim_node
```
and another runs the following commands (from the catkin_ws directory)
```
source /devel/setup.bash
rosrun turtle_control turtle_movement.py turtle1
```
if you want to add in a turtle do(without the ""):
```
./newturtle.sh "turtle name"
```
## How to navigate the folders
#### Turtle movement
the turtle movement source code is in the src scripts directory named turtle_movement.py
#### Bash scripts
running new_turtle.sh creates a new turtle and lets the current terminal control the new turtle( make sure you have already ran rosrun turtlesim turtlesim_node command_

