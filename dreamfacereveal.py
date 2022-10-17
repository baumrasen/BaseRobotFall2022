# LEGO type:standard slot:1 autostart
import base_robot
import sys
from spike import MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to

br = base_robot.BaseRobot()
#Function for Resetting Yaw Angle
Debugging = True
def debug(text):
    if Debugging:
        print(text)
def ResetGyro():
    br.hub.motion_sensor.reset_yaw_angle()
#Set Attachment Motors
attachment = MotorPair(br._leftAttachmentMotorPort,br._rightAttachmentMotorPort)
debug("Drive forward on left")
br.AccelGyroDriveForward(70)
ResetGyro()
debug("Turn Right")
br.GyroTurn(90)
debug("Move a small amount")
br.driveMotors.move_tank(14, 'cm', 50, 50)
ResetGyro()
debug("Turn Back")
br.GyroTurn(-83)
ResetGyro()
debug("Rotate Attachment")
attachment.move_tank(.9, 'rotations' ,-25, -25)
debug("Pick up Next Unit")
br.AccelGyroDriveForward(20)
ResetGyro()
br.GyroTurn(59)
br.driveMotors.move_tank(1.3, 'rotations', 55, 55)
ResetGyro()
br.GyroTurn(65)
ResetGyro()
br.AccelGyroDriveForward(40)
ResetGyro()
attachment.move_tank(.9, 'rotations' ,25, 25)
br.GyroTurn(69)
ResetGyro()
br.driveMotors.move_tank(6, 'rotations', 100, 90)