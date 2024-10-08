#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import sys, select, termios, tty
from turtlesim.srv import SetPen

SPEED =3
# Key mappings
move_bindings = {
    'w': (SPEED, 0, 0, 0),
    's': (-SPEED, 0, 0, 0),
    'a': (0, 0, SPEED, 0),
    'd': (0, 0, -SPEED, 0),
}

def get_key():#to read inputs from the user without having to press enter
    tty.setraw(sys.stdin.fileno()) #switch terminal into raw mode, terminal reads byte by byte without buffering
    select.select([sys.stdin], [], [], 0) #to see if there is any input
    key = sys.stdin.read(1) #to read a byte from the terminal
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings) 
    return key

def main():

    args = rospy.myargv(argv=sys.argv)
    try:
        turtle_name = args[1]
    except IndexError:

        turtle_name = "turtle1"

    rospy.init_node(f'{turtle_name}_wasd_control')

    pub_ctrl = rospy.Publisher(f'/{turtle_name}/cmd_vel', Twist, queue_size=10) #publishes the movement of the turtle
    pub_atck = rospy.Publisher('/attack',String,queue_size=10) #publishes when to attack

    print("Hello", turtle_name)

    rospy.wait_for_service(f'/{turtle_name}/set_pen')

    set_pen = rospy.ServiceProxy(f'/{turtle_name}/set_pen', SetPen)

    set_pen(255,255,255,0,1)
    
    global settings
    settings = termios.tcgetattr(sys.stdin) #takes current settings of the terminal

    print("Use WASD keys to move the turtle!")
    print("Type q to attack")
    print("Press Ctrl+C to exit.")

    while not rospy.is_shutdown():
        key = get_key()

        if key in move_bindings.keys():
            x, y, z, th = move_bindings[key]
        else:
            x, y, z, th = 0, 0, 0, 0
            if key =='q':
                string = String()
                string.data=turtle_name
                pub_atck.publish(string)
            elif key == '\x03':  # Ctrl+C
                break

        twist = Twist()
        twist.linear.x = x
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = z

        pub_ctrl.publish(twist)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
