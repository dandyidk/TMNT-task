#!/bin/bash



rosservice call /spawn 2 2 0 $1

./src/turtle_control/scripts/add-turtle.sh $1

source devel/setup.bash

sleep 2

rosrun turtle_control turtle_movement.py $1

