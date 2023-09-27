#! /usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import \
    TransformStamped, Transform, Quaternion, Point
import numpy as np
# import math as np

if __name__ == '__main__':

    rospy.init_node('tf_subscriber')

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rospy.sleep(1)

    frame_1 = tf_buffer.lookup_transform(
        'world',
        'frame_1',
        rospy.Time(0)
    )

    rospy.loginfo(frame_1)
