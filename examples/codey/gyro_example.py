from makeblock.boards import Codey

# Connect to the Codey board
board = Codey.connect("COM3")

# Read gyro sensor values from the Codey board
gyro_x = board.gyro.get_x()
gyro_y = board.gyro.get_y()
gyro_z = board.gyro.get_z()

print("Gyro X:", gyro_x)
print("Gyro Y:", gyro_y)
print("Gyro Z:", gyro_z)
