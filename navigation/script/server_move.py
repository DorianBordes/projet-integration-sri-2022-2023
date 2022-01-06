#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys
import time
import os

import actionlib
import actionlib_tutorials.msg
import navigation.msg
import std_msgs

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion, PoseStamped
from navigation.srv import *


pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)

def handle_move(req):
    rospy.loginfo(req)
    pose = PoseStamped()
    pose.header = std_msgs.msg.Header()
    pose.header.stamp = rospy.Time.now()
    pose.header.frame_id = "map" 
    pose.pose = Pose()
    pose.pose.position.x = req.x #  kinect Z value, [2], is X in TF of camera_link
    pose.pose.position.y = req.y # kinect X value, [0], is -Y in TF of camera_link
    pose.pose.position.z = req.z # kinect Y value, [1], is -Z in TF of camera_link
    pose.pose.orientation.x = req.xr
    pose.pose.orientation.y = req.yr
    pose.pose.orientation.z = req.zr 
    pose.pose.orientation.w = req.wr
    pub.publish(pose)
    return 0


def add_move_server():
    
    rospy.init_node('move_base_server')
    s = rospy.Service('move_base',move_base,handle_move)
    rospy.spin()

if __name__=="__main__":
    add_move_server()