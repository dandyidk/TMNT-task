#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String
import sys
#hello
class TurtleTracker:
    def __init__(self):

        rospy.init_node("turtle_tracker",anonymous = True)
        arg = rospy.myargv(argv=sys.argv) #must add in all turtle names as arguments
        self.turtles_tracker = {}
        for i in arg[1:]:
            self.turtles_tracker[i] = {'x':2,
                                       'y':2} #this variable holds all the positions of all turtles
            #simply type in self.turtles.tracker[turtlename]['x' or 'y']
        self.subscribers = {} #for subscribing all turtles
        for i in arg[1:]:
            self.subscribers[i] = rospy.Subscriber(f'{i}/pose',Pose,self.callback,callback_args= i)

        self.pose = Pose()
        rospy.Subscriber('/attack',String,self.attack)
    def callback(self,data,name):
        self.turtles_tracker[name] = {
            'x':data.x,
            'y':data.y
        }
    def attack(self,data):
        print(data.data)
        
    def run(self):
        rospy.spin()
if __name__ == '__main__':
    tracker = TurtleTracker()
    tracker.run()
