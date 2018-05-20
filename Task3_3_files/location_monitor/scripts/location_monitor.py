#!/usr/bin/env python

## Simple location monitor node that publishes three topics with the following information:
## -> closestObject: closest object to the robot and the distance
## -> robotPosition: position x and y of the robot
## -> targetLandmark: show a message when the robot is near or outside a specific set of landmarks

import rospy
import math
from nav_msgs.msg import Odometry 
from std_msgs.msg import String

pub = rospy.Publisher('closestObject',String, queue_size=100)
pubnear = rospy.Publisher('targetLandmark',String,queue_size=10)
pubpos = rospy.Publisher('robotPosition',String,queue_size=10)
 
current = 'none'

centerObj ={'dumpster':[-0.11,-2.67],'cylinder': [-1.27,-2.88],'bookshelf':[0.07,0.48],'barrier':[-2.93,-0.89],'cube':[0.13,-1.03]}

def callback(data):
    
    global current
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
   
    pubpos.publish('x: '+str(x)+',y: '+str(y))
    
    closest =[float('inf'),'none']	 
    for i in centerObj:
	d=math.sqrt((x-centerObj[i][0])**2+(y-centerObj[i][1])**2)
        if (d<closest[0]):
        	closest[0]=d
		closest[1]=i
    	if ( (d<=0.5) and (current!=i)):
		pubnear.publish('I am near the '+i)
		current = i
    if ((closest[0]>0.5) and (current != 'none')):
	current ='none'
	
	pubnear.publish('I am outside the regions')
    pub.publish('name: ' + closest[1] + ' , d: ' + str(closest[0]) )

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('odom', Odometry, callback) #change topic

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
