from makeblock.boards import meorion
from time import sleep

# Connect to the MeOrion board
board = meorion.connect()

# Set the color of the LED to red
board.set_led(0, 255, 0, 0)
sleep(1)

# Set the color of the LED to green
board.set_led(0, 0, 255, 0)
sleep(1)

# Set the color of the LED to blue
board.set_led(0, 0, 0, 255)
sleep(1)
