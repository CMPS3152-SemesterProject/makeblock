import makeblock
from makeblock.boards import mBuild

# Add the COM port
makeblock.add_port("COM3")

# Connect to the mBuild board
board = mBuild.connect()

# Control a DC motor
motor = board.dcmotor(1)
motor.set_pwm(100)  # Run the motor at full speed
