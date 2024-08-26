#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys
#hello
class TurtleTracker:
    def __init__(self):

        rospy.init_node("turtle_tracker",anonymous = True)
        arg = rospy.myargv(argv=sys.argv)
        self.turtles_tracker = {}
        for i in arg[1:]:
            self.turtles_tracker[i] = {'x':2,
                                       'y':2}
        self.subscribers = {}
        for i in arg[1:]:
            self.subscribers[i] = rospy.Subscriber(f'{i}/pose',Pose,self.callback,callback_args= i)

        self.pose = Pose()
        for i in arg[1:]:
            print(self.turtles_tracker[i]['x'])
    def callback(self,data,name):
        self.turtles_tracker[name] = {
            'x':data.x,
            'y':data.y
        }
        
    def run(self):
        rospy.spin()
if __name__ == '__main__':
    tracker = TurtleTracker()
    tracker.run()
