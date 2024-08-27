#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String
import sys,math

RADIUS = 10.4

class TurtleTracker:
    def __init__(self):

        rospy.init_node("turtle_tracker",anonymous = True)
        arg = rospy.myargv(argv=sys.argv) #must add in all turtle names as arguments

        self.turtles_tracker = {}
        self.subscribers = {} #for subscribing all turtles

        for i in arg[1:]:
            self.turtles_tracker[i] = {'x':2,
                                       'y':2,
                                       'health' :100,
                                       'attack':10} #this variable holds all the information of all turtles
            #simply type in self.turtles.tracker[turtlename]['info']
            self.subscribers[i] = rospy.Subscriber(f'{i}/pose',Pose,self.callback,callback_args= i)

        self.pose = Pose()
        rospy.Subscriber('/attack',String,self.attack)
    def callback(self,data,name):
        self.turtles_tracker[name] = {
            'x':data.x,
            'y':data.y
        }
    def attack(self,data):
        name = data.data
        turtle = self.turtles_tracker[name]
        self.turtles_tracker[name] ={'attack':1}
        for i in self.turtles_tracker:
            print(i)
            oppturtle=self.turtles_tracker[i]
            if i == name:
                continue
            else:
                print(turtle['x'],turtle['y'])
                print(oppturtle['x'],oppturtle['y'])
                x =abs(turtle['x']-oppturtle['x'])
                y =abs(turtle['y']-oppturtle['y'])
               
                hypo = math.sqrt(pow(x,2)+pow(y,2))
                if RADIUS<hypo:
                    oppturtle['health'] -= 50
                    print(oppturtle['health'])


        
    def run(self):
        rospy.spin()
if __name__ == '__main__':
    tracker = TurtleTracker()
    tracker.run()
