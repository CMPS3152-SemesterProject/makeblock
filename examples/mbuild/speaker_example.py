import makeblock
from makeblock.boards import mBuild

# Add the COM port
makeblock.add_port("COM3")

# Connect to the mBuild board
board = mBuild.connect()

# Play a sound using the speaker module
speaker = board.speaker(1)
speaker.play_tone(440)  # Play a 440 Hz tone
