import makeblock
from makeblock.boards import mcore

# Add the COM port
makeblock.add_port("COM3")

# Connect to the mCore board
board = mcore.connect()

# Read sensor data from the light sensor
def read_light_sensor():
    def callback(value):
        print("Light sensor value:", value)
    board.get_lightness(callback)

# Read sensor data from the button
def read_button():
    def callback(value):
        print("Button pressed:", value)
    board.is_pressed(callback)

# Main function to read sensor data
def main():
    while True:
        read_light_sensor()
        read_button()
        sleep(1)

if __name__ == "__main__":
    main()
