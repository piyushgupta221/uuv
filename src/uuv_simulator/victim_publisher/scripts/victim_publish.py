#!/usr/bin/env python

from __future__ import print_function
import rospy
from copy import deepcopy
from geometry_msgs.msg import PointStamped, Point
from visualization_msgs.msg import Marker, MarkerArray
import numpy as np


class victim_mark:

    def __init__(self):
        self._namespace = rospy.get_namespace().replace('/', '')        
        self._victim_markers = MarkerArray()  
        self._label_marker = Marker()
        self._label_marker.header.frame_id = 'world'
        self._label_marker.ns = self._namespace
        self._label_marker.type = Marker.SPHERE
        self._label_marker.action = Marker.ADD
        self._label_marker.pose.orientation.x = 0.0
        self._label_marker.pose.orientation.y = 0.0
        self._label_marker.pose.orientation.z = 0.0
        self._label_marker.pose.orientation.w = 1.0
        self._label_marker.scale.x = 2.0
        self._label_marker.scale.y = 2.0
        self._label_marker.scale.z = 2.0
        self._label_marker.color.a = 1.0
        self._label_marker.color.r = 1.0
        self._label_marker.color.g = 0.0
        self._label_marker.color.b = 0.0
        self._label_marker.lifetime = rospy.Duration()
        self._user_click_sub = rospy.Subscriber('/clicked_point', PointStamped, self.victim_mark_callback)
        self._victim_pub = rospy.Publisher('/marked_victims', MarkerArray, queue_size=10)
    

    def victim_mark_callback(self, msg):
        new_marker = deepcopy(self._label_marker)
        new_marker.header.stamp = rospy.Time.now()
        new_marker.id=len(self._victim_markers.markers)
        new_marker.pose.position.x = msg.point.x
        new_marker.pose.position.y = msg.point.y
        new_marker.pose.position.z = msg.point.z
        self._victim_markers.markers.append(new_marker)
        #self._victim_pub.publish(self._victim_markers)

if __name__ == '__main__':
    rospy.init_node('victim_publish')

    try:
        Victims = victim_mark()
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            Victims._victim_pub.publish(Victims._victim_markers)
            rate.sleep()
        # rospy.spin()
    except rospy.ROSInterruptException:
        print('caught exception')
    print('exiting')
