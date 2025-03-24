from makeblock.boards import RJ25N

# Connect to the RJ25N board
board = RJ25N.connect("COM3")

# Control a motor
motor = board.DCMotor(1)
motor.run(100)  # Run the motor at full speed
