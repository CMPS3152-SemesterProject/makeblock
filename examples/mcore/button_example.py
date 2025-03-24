import makeblock
from makeblock.boards import mcore

# Add the COM port
makeblock.add_port("COM3")

# Connect to the mCore board
board = mcore.connect()

# Check if the button is pressed
def check_button():
    def callback(value):
        if value:
            print("Button is pressed")
        else:
            print("Button is not pressed")
    board.is_pressed(callback)

# Main function to check the button status
def main():
    while True:
        check_button()
        sleep(1)

if __name__ == "__main__":
    main()
