from makeblock.boards import halocode
from time import sleep

# Connect to the Halocode board
board = halocode.connect()

# Set the color of the LED to red
board.set_led(0, 255, 0, 0)
sleep(1)

# Set the color of the LED to green
board.set_led(0, 0, 255, 0)
sleep(1)

# Set the color of the LED to blue
board.set_led(0, 0, 0, 255)
sleep(1)
