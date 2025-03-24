import makeblock
from makeblock.boards import MeAuriga

# Add the COM port
makeblock.add_port("COM3")

# Connect to the MeAuriga board
board = MeAuriga.connect()

# Read the temperature from the onboard sensor
temperature = board.get_temperature()
print("Temperature:", temperature)
