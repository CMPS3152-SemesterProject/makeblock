import makeblock
from makeblock.boards import Neuron
from time import sleep

# Add the COM port
makeblock.add_port("COM3")

# Connect to the Neuron board
board = Neuron.connect()

# Set the color of the LED to red
board.set_color(255, 0, 0)
sleep(1)

# Set the color of the LED to green
board.set_color(0, 255, 0)
sleep(1)

# Set the color of the LED to blue
board.set_color(0, 0, 255)
sleep(1)
