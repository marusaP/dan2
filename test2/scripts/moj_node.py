#!/usr/bin/env python

import rospy

if __name__ == '__main__':
  rospy.init_node('my_first_python_node', anonymous = True)
  rospy.loginfo('This node has been started.')
  rospy.sleep(100)
  print('Exit now')