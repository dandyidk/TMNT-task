## To run the game

One terminal runs
```
$ roscore
```
Another runs
```
$ rosrun turtlesim turtlesim_node
```
and another runs the following commands (from the catkin_ws directory)
```
./setup.sh
```
if you want to add in/take control of a turtle do (without the ""):
```
$ ./new_turtle.sh "TURTLE NAME"
```
if u want to track all turtles positions:
```
$ rosrun turtle_control turtle_tracker "ALL TURTLE NAMES YOU WANT TO TRACK"
```
## How to navigate the folders
#### turtle movement and turtle tracker
the turtle movement and tracker source codes are in the src scripts directory named turtle_movement.py
#### Bash scripts
running new_turtle.sh creates a new turtle ( make sure you have already ran rosrun turtlesim turtlesim_node command_

