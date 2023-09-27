#! /usr/bin/env python

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
    stored_data = {}

    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = "trans.dat"
    outfile = open(file_name,'wb')
    saved_data = {}
    #########################
    ##### STUDENT WRITES ####
    #########################
    transformation = tf_buffer.lookup_transform('world', 'frame_2', rospy.Time(0))

    saved_data['world_fr2'] = transformation

    # Hint - Use the tf_buffer.lookup_transform() method to retrieve the transform.
    # Example:
    # transformation = tf_buffer.lookup_transform(from_frame, to_frame, rospy.Time(0))
    # Note - from_frame and to_frame need to be defined!

    #########################

    pickle.dump(saved_data, outfile)
    outfile.close()

    '''Write a Python script that stores the transformation between one frame (e.g. world) and another (e.g. frame_2) 
    into a Pickle file (make up an extension, for example .dat).'''