import makeblock
from makeblock.boards import MegaPi

# Add the COM port
makeblock.add_port("COM3")

# Connect to the MegaPi board
board = MegaPi.connect()

# Control a DC motor
motor = board.dcmotor(1)
motor.run(100)  # Run the motor at full speed
