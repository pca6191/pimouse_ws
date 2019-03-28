#!/usr/bin/env python

#motors.py
#Copyright (c) 2016 Ryuichi Ueda <ryuichiueda@gmail.com>
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php

import rospy,copy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

class WallStop():
    def __init__(self):
        self.cmd_vel = rospy.Publisher('/raspimouse_on_gazebo/diff_drivcontroller/cmd_vel',Twist,queue_size=1)

    def run(self):
        rate = rospy.Rate(1)
        data = Twist()

        while not rospy.is_shutdown():
            data.linear.x = 0.2
            data.angular.z = 0

            self.cmd_vel.publish(data)
            rate.sleep()
            

if __name__ == '__main__':
    rospy.init_node('my_wall_stop')
    pub = rospy.Publisher('/raspimouse_on_gazebo/diff_drive_controller/cmd_vel', Twist, queue_size=1)
    try:
        while not rospy.is_shutdown():
            vel = Twist()
            direction = raw_input('w: forward, s: backward, a: left, d: right, q: quit > ')
            if 'w' in direction:
                vel.linear.x = 0.18
            if 's' in direction:
                vel.linear.x = -0.18
            if 'a' in direction:
                vel.angular.z = 90*3.14/180.0
            if 'd' in direction:
                vel.angular.z = -90*3.14/180.0
            if 'q' in direction:
                break
            print vel
            pub.publish(vel)
    except rospy.ROSInterruptException:
            pass

    #w = WallStop()
    #w.run()
