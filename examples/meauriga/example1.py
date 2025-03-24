import makeblock
from makeblock.boards import MeAuriga
from time import sleep

# Add the COM port
makeblock.add_port("COM3")

# Connect to the MeAuriga board
board = MeAuriga.connect()

# Set the color of an RGB LED
board.set_color(1, 255, 0, 0)
sleep(1)
board.set_color(1, 0, 255, 0)
sleep(1)
board.set_color(1, 0, 0, 255)
sleep(1)
board.set_color(1, 255, 255, 255)
