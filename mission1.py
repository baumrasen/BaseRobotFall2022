# LEGO type:standard slot:0 autostart

import base_robot
import sys
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to


br = base_robot.BaseRobot()
br.hub.motion_sensor.reset_yaw_angle()

br.AccelGyroDriveForward(60)
br.TurnRightAndDriveOnHeading(60, 90)
br.TurnRightAndDriveOnHeading(30, 120)

# br.hub.light_matrix.show_image("ARROW_S")
# br.leftMedMotor.run_for_seconds(2, 100)
# br.leftMedMotor.run_for_seconds(2, -100)
# br.leftMedMotor.set_stop_action("coast")
# br.leftMedMotor.stop()

# br.hub.light_matrix.show_image("ARROW_N")
# br.rightMedMotor.run_for_seconds(2, 100)
# br.rightMedMotor.run_for_seconds(2, -100)
# br.rightMedMotor.set_stop_action("coast")
# br.rightMedMotor.stop()
# br.debuggingEnabled = True
# br.GyroTurn(90)

#back up gently to make sure the robot is square in the jig
#then reset the gyro
#br.driveMotors.move(.5, "seconds", 0, -10)
# br.hub.motion_sensor.reset_yaw_angle()

# #br.driveMotors.move_tank(40, 'cm', 70, 70)

# br.AccelGyroDriveForward(50)
# br.TurnRightAndDriveOnHeading(45, 110)

# #br.driveMotors.move_tank(60, "cm", 10, 10)
# wait_for_seconds(0.2)

# curHead = br.hub.motion_sensor.get_yaw_angle()
# print("Robot stopped. Current heading is " + str(curHead))


#raise SystemExit
#sys.exit("All done. This is a normal exit.")

