#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def forward():
    pub.publish("linear: x: 1.0 y: 0.0 z: 0.0 angular: x: 0.0 y: 0.0 z: 0.0")


if __name__ == '__main__':

    rospy.init_node('task1_gazebo', anonymous=True)
    rate = rospy.Rate(5)
    pub = rospy.Publisher('/my_husky/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)
    rospy.spin()
    #forward()
