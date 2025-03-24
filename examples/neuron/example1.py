import makeblock
from makeblock.boards import Neuron

# Add the COM port
makeblock.add_port("COM3")

# Connect to the Neuron board
board = Neuron.connect()

# Control a motor
motor = board.dcmotor(1)
motor.run(100)  # Run the motor at full speed
