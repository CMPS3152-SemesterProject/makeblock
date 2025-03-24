from makeblock.boards import mBuild

# Connect to the mBuild board
board = mBuild.connect("COM3")

# Control a DC motor
motor = board.dcmotor(1)
motor.set_pwm(100)  # Run the motor at full speed
