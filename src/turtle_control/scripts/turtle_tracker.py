#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String
import sys,math
from turtlesim.srv import Kill
import time
RADIUS = 1

class TurtleTracker:
    def __init__(self):
        self.start_time=time.time() #for elapsing time
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

        rospy.wait_for_service('/kill')
        self.kill_turtle = rospy.ServiceProxy('/kill', Kill)


    def callback(self,data,name):
        self.turtles_tracker[name]['x'] = data.x
        self.turtles_tracker[name]['y'] = data.y


    def attack(self,data):
        name = data.data
        turtle = self.turtles_tracker[name]
        if turtle['attack']<0 or time.time() -self.start_time<1:
            return
        turtle['attack'] -=1
        self.start_time = time.time()
        for i in self.turtles_tracker:
            oppturtle=self.turtles_tracker[i]
            if i == name:
                continue
            else:
                x =abs(turtle['x']-oppturtle['x'])
                y =abs(turtle['y']-oppturtle['y'])
               
                hypo = math.sqrt(pow(x,2)+pow(y,2))
                if RADIUS>hypo:
                    print(name,"attacked ",oppturtle)
                    oppturtle['health'] -= 50
                    if oppturtle['health'] <= 0:
                        print(f"{i} has been killed!")
                        self.kill_turtle(i)
                        del self.turtles_tracker[i]  
                        break

        if self.gameover():
            print(self.gameover(),"Won")
            exit 


        
    def gameover(self):
        if len(self.turtles_tracker) <=1:
            for i in self.turtles_tracker:
                return i
        else:
            winner = 0
            for i in self.turtles_tracker:
                if self.turtles_tracker[i]["health"]>winner:
                    winner = i
                if self.turtles_tracker[i]["attack"] > 0:
                    return 0
            return winner
    
    def run(self):
        rospy.spin()
if __name__ == '__main__':
    tracker = TurtleTracker()
    tracker.run()
