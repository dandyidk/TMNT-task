#!/bin/bash

if ! grep -q "$1" "/home/dandy/catkin_ws/TMNT-task/src/turtle_control/text/allturtles.txt";then

	echo "$1" >> "/home/dandy/catkin_ws/TMNT-task/src/turtle_control/text/allturtles.txt" 
fi
