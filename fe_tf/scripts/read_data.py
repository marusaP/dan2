#! /usr/bin/env python

import rospy
import pickle
import tf2_ros
from geometry_msgs.msg import TransformStamped

if __name__ == '__main__':

    # Init the node
    rospy.init_node('tf_loader')

    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = 'trans.dat'

    infile = open(file_name,'rb')
    stored_poses = pickle.load(infile)
    infile.close()

    #########################
    ##### STUDENT WRITES ####
    #########################
    tf_broad = tf2_ros.StaticTransformBroadcaster()

    tr = stored_poses['world_fr2']

    print (tr)
    tf_broad.sendTransform([tr])

    #for key, value in tr: 
    #    tf_broad.sendTransform(value)

    #stored_poses.keys()    .values(), .items()

    #########################
    rospy.spin()


    '''Write a Python scrip that will read the Pickle file produced by the saver script and publish the transforms onto TF. 
    We don't expect these frames to change in the future. You can therefore use the StaticTransformBroadcaster() class to publish them.'''