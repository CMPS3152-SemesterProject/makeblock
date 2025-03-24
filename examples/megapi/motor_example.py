from makeblock.boards import MegaPi

# Connect to the MegaPi board
board = MegaPi.connect("COM3")

# Control a DC motor
motor = board.dcmotor(1)
motor.run(100)  # Run the motor at full speed
