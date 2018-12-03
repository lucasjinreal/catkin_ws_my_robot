#!/usr/bin/env python
#-*- coding:utf-8   -*-
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np


class Controller(object):

    def __init__(self):
        rospy.init_node('wander')

        self.scan_sub = rospy.Subscriber('scan', LaserScan, self.scan_callback)
        self.control_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

        self.g_range_ahead = 0.1
        # if > 0.2, change direction avoid obstacles
        self.min_obstacle_dist = 0.5
    

    def scan_callback(self, msg):
        # change the middle value into a angle range average value
        mid = len(msg.ranges) / 2

        wide = 1
        # print(msg.ranges[mid-wide:  mid+wide])
        self.g_range_ahead = np.min(msg.ranges[mid-wide:  mid+wide])
        if self.g_range_ahead == np.inf:
            self.g_range_ahead = 0.0
        # print('ahead obstacle distance: {}'.format(self.g_range_ahead))
    
    def run(self):
        r = rospy.Rate(1)
        while not rospy.is_shutdown():
            print('\nahead obstacle distance: {}'.format(self.g_range_ahead))
            twist = Twist()
            if self.g_range_ahead <= self.min_obstacle_dist:
                twist.angular.z = 0.5
                twist.linear.x = -0.5
                print('<-- backward  {}'.format(twist))
                self.control_pub.publish(twist)
            else:
                # forward
                twist.linear.x = 0.2
                print('--> forward  {}'.format(twist))
                self.control_pub.publish(twist)
            r.sleep()

if __name__ == '__main__':
    c = Controller()
    c.run()
