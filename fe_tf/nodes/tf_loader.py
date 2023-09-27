#! /usr/bin/env python

import rospy
import pickle

if __name__ == '__main__':

    # Init the node
    rospy.init_node('tf_loader')

    # Read the jar of pickles
    file_name = raw_input("Please wire the path of the pickle file:")
    infile = open(file_name,'rb')
    stored_poses = pickle.load(infile)
    infile.close()

    rospy.loginfo("Printing all the stored transforms.")
    for transform in stored_poses.values():
        rospy.loginfo(transform)


