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

# Read the temperature from the onboard sensor
temperature = board.get_temperature()
print("Temperature:", temperature)

# Read the lightness from the onboard sensor
lightness = board.get_lightness(1)
print("Lightness:", lightness)

# Read the roll, pitch, and yaw from the onboard sensor
roll = board.get_roll()
print("Roll:", roll)
pitch = board.get_pitch()
print("Pitch:", pitch)
yaw = board.get_yaw()
print("Yaw:", yaw)

# Connect sensors to the RJ45 port
ultrasonic_sensor = board.ultrasonic(1)
line_reader = board.linefollower(1)

# Read the distance from the ultrasonic sensor
distance = ultrasonic_sensor.read()
print("Distance:", distance)

# Read the line status from the line reader
line_status = line_reader.read()
print("Line Status:", line_status)

# Use the onboard button
button = board.button(1)
button_status = button.read()
print("Button Status:", button_status)
