#!/bin/bash



rosservice call /spawn 2 2 0 $1

sleep 4

rosrun turtle_control turtle_movement.py $1

