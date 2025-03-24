import makeblock
from makeblock.boards import RJ25N

# Add the COM port
makeblock.add_port("COM3")

# Connect to the RJ25N board
board = RJ25N.connect()

# Control a motor
motor = board.DCMotor(1)
motor.run(100)  # Run the motor at full speed
