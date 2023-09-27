#! /usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

if __name__ == '__main__':

    rospy.init_node('tf_static_broadcaster')

    tf_broad = tf2_ros.TransformBroadcaster()

    frame_1 = TransformStamped()
    frame_1.child_frame_id = 'frame_1'
    frame_1.header.frame_id = 'world'

    frame_1.transform.rotation.w = 1.0

    frame_1.transform.translation.z = 1.0
    frame_1.transform.translation.y = 0.0
    frame_1.transform.translation.x = 0.0

    rospy.loginfo("Publishing transform from {0} to {1}".format(frame_1.header.frame_id, frame_1.child_frame_id))
    rospy.sleep(0.1)
    tf_broad.sendTransform([frame_1])

    rospy.spin()
