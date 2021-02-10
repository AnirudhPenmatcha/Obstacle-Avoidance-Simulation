#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8
import cv2
from cv_bridge import CvBridge
import grid
import numpy as np

bridge = CvBridge()

def move_rover(direction, (velocity_publisher, vel_msg)):
    print("~~~~~~~~~~~~~~~~~INSIDE~~~~~~~~~~~~~~~~~~~~~~~~~~", direction.data)
    if direction.data == 0:
        vel_msg.linear.x = 1
        velocity_publisher.publish(vel_msg)
    elif direction.data == 1:
        vel_msg.linear.x = 0
        vel_msg.angular.z = 1
        velocity_publisher.publish(vel_msg)
        rospy.sleep(1.0)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

    elif direction.data == 2:
        vel_msg.linear.x = 0
        vel_msg.angular.z = -1
        velocity_publisher.publish(vel_msg)
        rospy.sleep(1.2)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)



def forward(vel_msg):
    vel_msg.linear.x = 1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

def cb2(frame, direction_pub):
    img = bridge.imgmsg_to_cv2(frame, desired_encoding='passthrough')
    direction = grid.detect_obstacle(img)
    direction_pub.publish(direction)


if __name__ == '__main__':
    rospy.init_node('task1_gazebo', anonymous=True)
    velocity_publisher = rospy.Publisher('/my_husky/cmd_vel', Twist, queue_size=10)
    direction_pub = rospy.Publisher('direction', Int8, queue_size = 10)
    rospy.sleep(0.1)
    vel_msg = Twist()

    sub = rospy.Subscriber("/camera/depth/image_raw",Image,cb2,direction_pub, queue_size = 1, buff_size = 2**24)
    direction_sub = rospy.Subscriber("direction",Int8,move_rover, (velocity_publisher, vel_msg))

    rospy.spin()
