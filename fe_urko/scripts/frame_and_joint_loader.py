#!/usr/bin/env python2


import rospy
import pickle
import tf2_ros
from geometry_msgs.msg import Pose
import moveit_commander

def transformstamped_to_pose(transform_stamped):
    """Convert from geometry_msgs/TransformStamped to geometry_msgs/Pose

    Args:
        transform_stamped (geometry_msgs/TransformStamped): The geometry_msgs/TransformStamped message to convert

    Returns:
        Pose: The geometry_msgs/Pose message
    """
    return Pose(position=transform_stamped.transform.translation, orientation=transform_stamped.transform.rotation)

def get_pose_from_tf(target, tf_buffer, relative_to='base_link'):
    """Return a Pose object to the desired TF frame

    Args:
        target (str): TF frame that we are interested in
        tf_buffer (tf2_ros.Buffer): A TF buffer. Don't forget to initialize it with the listener!!!
        relative_to (str, optional): Relative to ...

    Return:
        Pose: The TF frame expressed as geometry_msgs/Pose
    """

    rospy.sleep(0.1)
    target_transform = tf_buffer.lookup_transform(relative_to, target, rospy.Time(0))
    return transformstamped_to_pose(target_transform)

if __name__ == '__main__':

    rospy.init_node('tf_loader')

    file_name = input("Vnesi ime datoteke iz katere jemljes podatke: ")

    infile = open(file_name, 'rb')
    stored_poses = pickle.load(infile)
    infile.close()

    tf_broad = tf2_ros.StaticTransformBroadcaster()
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    moveit_interface = moveit_commander.MoveGroupCommander('manipulator')

    moveit_interface.set_max_velocity_scaling_factor(1.0)
    moveit_interface.set_max_accelerarion_scaling_factor(1.0)
    
    frames = []
    rospy.sleep(0.1)
    for joint, frame in stored_poses.values(): 
        print(joint, frame)
        frames.append(frame)

    tf_broad.sendTransform(frames)
    rospy.sleep(0.2)

    for entry in stored_poses: 
        moveit_interface.go(get_pose_from_tf(entry, tf_buffer),wait = True)

    for joint, _ in stored_poses.values():
        moveit_interface.go(joint,wait = True)

    rospy.spin()



