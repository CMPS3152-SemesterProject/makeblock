from makeblock.boards import MegaPiPro
from makeblock.comm import SerialPort

# Connect to the MegaPiPro board
uart = SerialPort.connect("COM3")
board = MegaPiPro.connect(uart)

# Control a servo motor
servo = board.servo(1)
servo.set_angle(90)  # Set the servo to 90 degrees
