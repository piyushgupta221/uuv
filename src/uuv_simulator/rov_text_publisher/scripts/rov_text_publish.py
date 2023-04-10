#!/usr/bin/env python

from __future__ import print_function
import rospy
from copy import deepcopy
from geometry_msgs.msg import PointStamped, Point
from visualization_msgs.msg import Marker, MarkerArray
import numpy as np


class rov_mark:

    def __init__(self):
        self._namespace = rospy.get_namespace().replace('/', '')        
        self._label_marker = Marker()
        self._label_marker.header.frame_id = 'world'
        self._label_marker.ns = self._namespace
        self._label_marker.type = Marker.TEXT_VIEW_FACING
        self._label_marker.text = self._namespace
        self._label_marker.action = Marker.ADD
        self._label_marker.pose.orientation.x = 0.0
        self._label_marker.pose.orientation.y = 0.0
        self._label_marker.pose.orientation.z = 0.0
        self._label_marker.pose.orientation.w = 1.0
        self._label_marker.scale.z = 3.0
        self._label_marker.color.a = 1.0
        self._label_marker.color.r = 1.0
        self._label_marker.color.g = 1.0
        self._label_marker.color.b = 0.0
        self._label_marker.lifetime = rospy.Duration()
        self._rov_pub = rospy.Publisher('/ROV_text', Marker, queue_size=10)
        if rospy.has_param('~x'):
            self._label_marker.pose.position.x = rospy.get_param('~x')
        if rospy.has_param('~y'):
            self._label_marker.pose.position.y = rospy.get_param('~y')
        if rospy.has_param('~z'):
            self._label_marker.pose.position.z = rospy.get_param('~z')
        

if __name__ == '__main__':
    rospy.init_node('rov_text_publish')

    try:
        ROV = rov_mark()
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            ROV._rov_pub.publish(ROV._label_marker)
            rate.sleep()
        # rospy.spin()
    except rospy.ROSInterruptException:
        print('caught exception')
    print('exiting')
