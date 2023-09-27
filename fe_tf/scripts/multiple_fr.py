#! /usr/bin/env python

import rospy
import tf2_ros
import math
import rospy
from geometry_msgs.msg import TransformStamped

if __name__ == '__main__':

    rospy.init_node('tf_broadcaster')

    tf_broad = tf2_ros.TransformBroadcaster()

    frame_1 = TransformStamped()
    frame_1.child_frame_id = 'frame_1'
    frame_1.header.frame_id = 'world'

    frame_1.transform.rotation.w = 1.0

    frame_1.transform.translation.z = 1.0
    frame_1.transform.translation.y = 0.0
    frame_1.transform.translation.x = 0.0

    frame_2 = TransformStamped()
    frame_2.child_frame_id = 'frame_2'
    frame_2.header.frame_id = 'frame_1'

    frame_2.transform.rotation.w = 1.0

    

    while not rospy.is_shutdown():

        frame_2.transform.translation.z = math.cos(rospy.get_time())
        frame_2.transform.translation.y = 0.0
        frame_2.transform.translation.x = math.sin(rospy.get_time())

        tf_broad.sendTransform([frame_1, frame_2])
        rospy.sleep(0.01)