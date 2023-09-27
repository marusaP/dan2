#! /usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

if __name__ == '__main__':

    rospy.init_node('tf_static_broadcaster')

    tf_broad = tf2_ros.StaticTransformBroadcaster()

    frame_1 = TransformStamped()
    frame_1.child_frame_id = 'frame_1'
    frame_1.header.frame_id = 'world'

    frame_1.transform.rotation.w = 1.0

    frame_1.transform.translation.z = 0.0
    frame_1.transform.translation.y = 0.0
    frame_1.transform.translation.x = 1.0


    frame_2 = TransformStamped()
    frame_2.child_frame_id = 'frame_2'
    frame_2.header.frame_id = 'frame_1'

    frame_2.transform.rotation.w = 1.0

    frame_2.transform.translation.z = 1.0
    frame_2.transform.translation.y = 0.0
    frame_2.transform.translation.x = 0.0

    rospy.loginfo("Publishing transform from {0} to {1}".format(frame_1.header.frame_id, frame_1.child_frame_id))
    tf_broad.sendTransform([frame_1, frame_2])

    rospy.spin()


    '''publishes three frames: world, frame_1 and frame_2. The relations between them should be as follows: - 
    frame_1 is offset by 1m along the Z axis from world - frame_2 is offset by 1m along the X axis from frame_1'''