from makeblock.boards import Codey

# Connect to the Codey board
board = Codey.connect("COM3")

# Read sensor data from the Codey board
temperature = board.temperature.get_temperature()
print("Temperature:", temperature)

lightness = board.light.get_lightness()
print("Lightness:", lightness)

button_pressed = board.button.is_pressed()
print("Button pressed:", button_pressed)
