from makeblock.boards import MeAuriga

# Connect to the MeAuriga board
board = MeAuriga.connect("COM3")

# Read the temperature from the onboard sensor
temperature = board.get_temperature()
print("Temperature:", temperature)
