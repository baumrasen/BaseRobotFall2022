# LEGO type:standard slot:15 autostart

import sys
import utime
from spike import (MotionSensor, MotorPair)
from spike.control import wait_for_seconds

f = open("log2.txt", "a")
debugMode = True
_leftDriveMotorPort = 'E'
_rightDriveMotorPort = 'A'
driveMotors = MotorPair(_leftDriveMotorPort,
                                _rightDriveMotorPort)

def Log(topic, msg):
    # Example usage
    # Log("GyroTurn", "Starting a gyro turn")
        #t = '%4d-%02d-%02d %02d:%02d:%02d' % utime.localtime() [:6]
        t = utime.ticks_ms()
        f.write(str(t) + " [" + topic + "] " + msg)
    #f.close()

def GyroTurn(angle):
    """
    Turns the robot to the specified `angle`. 
    Positive numbers turn to the right, negative numbers turn the \
    robot to the left. Note that when the robot makes the turn, it \
    will always overshoot by about seven degrees. In other words if \
    you need a +90 degree turn, you will probably end up commanding \
    something around +83 degrees. You may also want to put a \
    wait_for_seconds(0.2) or something like that after a gyro turn. \
    Just to make sure the robot has stopped moving before continuing \
    with more instructions.
    Parameter
    -------------
    angle: Where the robot should stop turning at. \
        Positive values turn the robot to the right, negative values \
        turn to the left.
    type: float
    values: Any. Best to keep the numbers less than 180, just so the \
        robot doesn't turn more than necessary.
    default: No default value
    """

    # open output file for logging
    if debugMode:
        Log("Gyroturn", "Turning to heading " + str(angle) + "\n")

    # Reset Yaw Angle
    MotionSensor().reset_yaw_angle()
    # Tests for angle and debug mode
    if debugMode and (angle > 179 or angle < -180):
        sys.exit("GyroTurn() Error: Angle must be between -180 \
            and 180")
    # Sets turn speed
    gyroTurnSpeed = 10
    # Tests if the angle is positive.
    yawAngle = MotionSensor().get_yaw_angle()
    if (angle > 0):
        driveMotors.start_tank(gyroTurnSpeed, -gyroTurnSpeed)
        while (yawAngle < angle):
            # If it it is positive it starts turning right.
            yawAngle = MotionSensor().get_yaw_angle()
            if (debugMode == True):
                Log("Gyroturn", "Current heading " + str(yawAngle) + "\n")
    else:
        driveMotors.start_tank(-gyroTurnSpeed, gyroTurnSpeed)
        while (yawAngle > angle):
            # If it it is positive it starts turning right.
            yawAngle = MotionSensor().get_yaw_angle()
            if (debugMode == True):
                Log("Gyroturn", "Current heading " + str(yawAngle) + "\n")

    # Stops when it is it has reached the desired angle
    if (debugMode == True):
        Log("Gyroturn", "Calling stop(). Current heading " + str(MotionSensor().get_yaw_angle()) + "\n")
    driveMotors.stop()
    if (debugMode == True):
        Log("Gyroturn", "stop() has been called. Current heading " + str(MotionSensor().get_yaw_angle()) + "\n")
    wait_for_seconds(0.5)
    if (debugMode == True):
        Log("Gyroturn", "Final heading " + str(MotionSensor().get_yaw_angle()) + "\n")


# Now, the test program

GyroTurn(45)
wait_for_seconds(1)
GyroTurn(-45)

f.close()