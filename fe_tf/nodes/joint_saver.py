#! /usr/bin/env python

from sensor_msgs.msg import JointState
import rospy
import pickle
import os

def joints_to_global(msg):
    global current_joints
    current_joints = msg

if __name__ == '__main__':

    rospy.init_node('joint_saver')
    rospy.loginfo("Joint saver started!")

    rospy.Subscriber('/joint_states', JointState, joints_to_global)

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

        saved_data[user_input] = current_joints

    rospy.loginfo("Storing the following entries: {}".format(saved_data.keys()))

    pickle.dump(saved_data, outfile)
    outfile.close()