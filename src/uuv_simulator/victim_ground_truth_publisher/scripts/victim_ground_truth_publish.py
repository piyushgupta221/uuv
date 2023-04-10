#!/usr/bin/env python3

from __future__ import print_function
import rospy
from copy import deepcopy
from geometry_msgs.msg import PointStamped, Point
from visualization_msgs.msg import Marker, MarkerArray
import numpy as np
from gazebo_msgs.msg import ModelStates


class victim_ground_truth_mark:
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
        self._label_marker.scale.x = 5.0
        self._label_marker.scale.y = 5.0
        self._label_marker.scale.z = 5.0
        self._label_marker.color.a = 1.0
        self._label_marker.color.r = 0.0
        self._label_marker.color.g = 1.0
        self._label_marker.color.b = 0.0
        self._label_marker.lifetime = rospy.Duration()
        self._user_click_sub = rospy.Subscriber('/gazebo/model_states', ModelStates, self.victim_ground_truth_mark_callback)
        self._victim_pub = rospy.Publisher('/victims_ground_truth', MarkerArray, queue_size=10)
    

    def victim_ground_truth_mark_callback(self, msg):
        victim_markers = MarkerArray()
        all_models= msg.name  
        j=0
        victims= [k for k in all_models if 'person' in k]
        mines= [k for k in all_models if 'sea' in k]
        for i in range(len(all_models)):  
           if 'sea' in all_models[i]:  
               new_marker = deepcopy(self._label_marker)
               new_marker.header.stamp = rospy.Time.now()
               new_marker.id=j
               new_marker.pose.position.x = msg.pose[i].position.x
               new_marker.pose.position.y = msg.pose[i].position.y
               new_marker.pose.position.z = msg.pose[i].position.z
               victim_markers.markers.append(new_marker)
               #self._victim_pub.publish(self._victim_markers)
               j=j+1
        self._victim_markers = deepcopy(victim_markers)
        
        
if __name__ == '__main__':
    rospy.init_node('victim_ground_truth_publish')

    try:
        Victims = victim_ground_truth_mark()
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            Victims._victim_pub.publish(Victims._victim_markers)
            rate.sleep()
        # rospy.spin()
    except rospy.ROSInterruptException:
        print('caught exception')
    print('exiting')
