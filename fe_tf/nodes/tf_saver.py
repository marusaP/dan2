#! /usr/bin/env python

from geometry_msgs.msg import TransformStamped
import rospy
import pickle
import os
import tf2_ros

if __name__ == '__main__':

    rospy.init_node('tf_saver')
    rospy.loginfo("TF saver started!")

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rospy.sleep(1)

    frame_1 = tf_buffer.lookup_transform(
                'world', 'frame_1', rospy.Time(0))

    stored_data = {}

    file_name = raw_input("Please wire the path for the pickle file:")

    file_dir = file_name[:file_name.find(file_name.split('/')[-1])]
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    outfile = open(file_name,'wb')
    user_input = 'empty'
    saved_data = {}
    while user_input != 'y':
        user_input = raw_input("Please write the name for the joint entry:\n")
        if not user_input:
            if raw_input("Are you done with storing data and you want to quit? [y/n]").lower() == 'y':
                break

        frame = tf_buffer.lookup_transform(
                    'world', 'frame_1', rospy.Time(0))
        saved_data[user_input] = frame

    pickle.dump(saved_data, outfile)
    outfile.close()