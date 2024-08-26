#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

class TurtleTracker:
    def __init__(self):

        rospy.init_node("turtle_tracker",anonymous = True)
        arg = rospy.myargv(argv=sys.argv)
        self.turtles_tracker = {}
        for i in arg[1:]:
            self.turtles_tracker[i] = {'x':2,
                                       'y':2}
            
        self.subscribers = []
        for i in arg[1:]:
            self.subscriber = rospy.Subscriber(f'{i}/pose',Pose,self.callback(),callback_args= i)

        self.pose = Pose()

    def callback(self,data,name):
        self.turtles_tracker[name] = {
            'x':data.x,
            'y':data.y
        }
        print(self.turtles_tracker[name].x)
    def run(self):
        rospy.spin()
if __name__ == '__main__':
    tracker = TurtleTracker()
    tracker.run()
