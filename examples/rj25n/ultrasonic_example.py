import makeblock
from makeblock.boards import RJ25N

# Add the COM port
makeblock.add_port("COM3")

# Connect to the RJ25N board
board = RJ25N.connect()

# Read the distance from the ultrasonic sensor
def read_distance():
    def callback(value):
        print("Distance:", value)
    board.ultrasonic.request_distance(callback)

# Main function to read the distance
def main():
    while True:
        read_distance()
        sleep(1)

if __name__ == "__main__":
    main()
