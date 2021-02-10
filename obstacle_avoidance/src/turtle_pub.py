#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('task1_gazebo', anonymous=True)
    velocity_publisher = rospy.Publisher('/my_husky/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()



    #distance = input("Type your distance:")
    #isForward = input("Foward?: ")#True or False
    rospy.sleep(0.1)

    vel_msg.linear.x = 1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # while not rospy.is_shutdown():


    velocity_publisher.publish(vel_msg)
    rospy.sleep(1.0)
    vel_msg.linear.x = 0
    #Force the robot to stop
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':

        #Testing our function
    move()
    rospy.spin()
