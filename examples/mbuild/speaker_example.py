from makeblock.boards import mBuild

# Connect to the mBuild board
board = mBuild.connect("COM3")

# Play a sound using the speaker module
speaker = board.speaker(1)
speaker.play_tone(440)  # Play a 440 Hz tone
