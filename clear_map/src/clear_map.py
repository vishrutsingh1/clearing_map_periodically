#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty,EmptyRequest

rospy.init_node("clearing_map")
rospy.wait_for_service("/move_base/clear_costmaps")
clear_map = rospy.ServiceProxy("/move_base/clear_costmaps",Empty)
msg = EmptyRequest()
while not rospy.is_shutdown():

	clear_map(msg)
	rospy.sleep(10)



