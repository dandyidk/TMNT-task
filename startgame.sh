source devel/setup.bash

args=""

while IFS= read -r line

do
	args+="$line "
done < "/home/dandy/catkin_ws/TMNT-task/src/turtle_control/text/allturtles.txt"

args=$(echo "$args" | sed 's/ $//')

> "/home/dandy/catkin_ws/TMNT-task/src/turtle_control/text/allturtles.txt"

rosrun turtle_control turtle_tracker.py $args
