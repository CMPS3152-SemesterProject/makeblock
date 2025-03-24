import cyberpi

# Connect to the cyberpi board
cyberpi.connect()

# Set the LED color to red
cyberpi.led.on(255, 0, 0)
