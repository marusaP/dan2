#! /usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import \
    TransformStamped, Transform, Quaternion, Point
import numpy as np
# import math as np

if __name__ == '__main__':

    rospy.init_node('tf_broadcaster_2')

    tf_broad = tf2_ros.TransformBroadcaster()

    frame_1 = TransformStamped()
    frame_1.child_frame_id = 'frame_2'
    frame_1.header.frame_id = 'frame_1'

    frame_1.transform.rotation.w = 1.0

    frame_1.transform.translation.z = 0
    frame_1.transform.translation.y = -1.0
    frame_1.transform.translation.x = 1.0

    while not rospy.is_shutdown():
        frame_1.header.stamp = rospy.Time.now()
        frame_1.transform.translation.x = 0.5*np.sin(2*rospy.Time.now().to_sec() )
        frame_1.transform.translation.y = 0.5*np.cos(2*rospy.Time.now().to_sec())
        tf_broad.sendTransform([frame_1])
        rospy.sleep(0.01)

    # rospy.spin()

