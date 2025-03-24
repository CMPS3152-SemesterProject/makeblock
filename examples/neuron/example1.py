from makeblock.boards import Neuron

# Connect to the Neuron board
board = Neuron.connect("COM3")

# Control a motor
motor = board.dcmotor(1)
motor.run(100)  # Run the motor at full speed
