from makeblock.boards import meorion

# Connect to the MeOrion board
board = meorion.connect()

# Read the light sensor value
def read_light_sensor():
    def callback(value):
        print("Light sensor value:", value)
    board.light.read(callback)

# Main function to read the light sensor value
def main():
    while True:
        read_light_sensor()
        sleep(1)

if __name__ == "__main__":
    main()
