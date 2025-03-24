import makeblock
from makeblock.boards import MegaPiPro
from makeblock.comm import SerialPort

# Add the COM port
makeblock.add_port("COM3")

# Connect to the MegaPiPro board
uart = SerialPort.connect()
board = MegaPiPro.connect()

# Control a servo motor
servo = board.servo(1)
servo.set_angle(90)  # Set the servo to 90 degrees
