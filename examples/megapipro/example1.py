import makeblock
from makeblock.boards import MegaPiPro
from makeblock.comm import SerialPort

# Add the COM port
makeblock.add_port("COM3")

# Connect to the MegaPiPro board
uart = SerialPort.connect()
board = MegaPiPro.connect()

# Read sensor data
def read_sensor_data():
    temperature = board.temperature.get_temperature()
    lightness = board.light.read()
    return temperature, lightness

# Print sensor data
temperature, lightness = read_sensor_data()
print("Temperature:", temperature)
print("Lightness:", lightness)
