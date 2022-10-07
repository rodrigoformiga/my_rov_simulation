#! /usr/bin/env python3

import sys
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64

def joystickCallback(joyMsg):
    global command
    command = [joyMsg.axes[0], joyMsg.axes[1], joyMsg.axes[3], joyMsg.axes[4]]

def rov_controller():
    while not rospy.is_shutdown():
        command_truster1 = Float64()
        command_truster2 = Float64()
        command_truster3 = Float64()
        command_truster4 = Float64()
        command_truster5 = Float64()
        command_truster6 = Float64()

        command_truster1 = command[0] * 10000
        command_truster2 = command[0] * 10000
        command_truster3 = command[1] * 10000
        command_truster4 = command[1] * 10000
        command_truster5 = command[2] * 10000
        command_truster6 = command[2] * 10000
        # print(command_truster)
        vertical1.publish(command_truster1)
        vertical2.publish(command_truster2)
        horiz1.publish(command_truster3)
        horiz2.publish(command_truster4)
        horiz3.publish(command_truster5)
        horiz4.publish(command_truster6)


if __name__ == '__main__':
    try:
        rospy.init_node('servo_command')
        vertical1 = rospy.Publisher('/rov/joint1_velocity_controller/command', Float64, queue_size=1)
        vertical2 = rospy.Publisher('/rov/joint2_velocity_controller/command', Float64, queue_size=1)
        horiz1 = rospy.Publisher('/rov/joint3_velocity_controller/command', Float64, queue_size=1)
        horiz2 = rospy.Publisher('/rov/joint4_velocity_controller/command', Float64, queue_size=1)
        horiz3 = rospy.Publisher('/rov/joint5_velocity_controller/command', Float64, queue_size=1)
        horiz4 = rospy.Publisher('/rov/joint6_velocity_controller/command', Float64, queue_size=1)

        joystick_subscriber = rospy.Subscriber('/joy', Joy, joystickCallback, queue_size=10)
        command = [0,0,0,0]
        rov_controller()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        pass  