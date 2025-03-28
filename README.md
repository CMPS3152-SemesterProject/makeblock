# Makeblock Library (with Bluetooth support)

The Makeblock library is a Python package that provides an interface to interact with various Makeblock devices and modules. It includes support for different boards, communication protocols, and modules, allowing users to control and interact with Makeblock hardware using Python.

## Features

- Support for multiple Makeblock boards, including Halocode, MegaPi, mCore, MeAuriga, and more.
- Communication with Makeblock devices using SerialPort, mlink and Bluetooth (using [Jakeler/ble-serial](https://github.com/Jakeler/ble-serial) for the bridge and [paulakg4/com0com](https://github.com/paulakg4/com0com) for the VCOM and null-modem router).
- Control various modules such as RGB LEDs, motors, sensors, and more.
- Easy-to-use API for interacting with Makeblock hardware.

## Installation

You can install the Makeblock library using pip:

```bash
pip install makeblock
```

For more information and documentation, visit the [official Makeblock documentation](https://makeblock.com).

## Usage Examples

### Connecting to a Makeblock Board

```python
from makeblock import SerialPort
from makeblock.boards import MegaPi

# Connect to the MegaPi board using a serial port
uart = SerialPort.connect("COM3")
board = MegaPi.connect(uart)

# Set the color of an RGB LED
board.rgbled.set_color(1, 255, 0, 0)
```

### Controlling a Motor

```python
from makeblock.boards import MegaPi

# Connect to the MegaPi board
board = MegaPi.connect("COM3")

# Control a DC motor
motor = board.dcmotor(1)
motor.run(100)  # Run the motor at full speed
```

### Reading Sensor Data

```python
from makeblock.boards import Halocode

# Connect to the Halocode board
board = Halocode.connect("COM3")

# Read the temperature from the onboard sensor
temperature = board.temperature.get_temperature()
print("Temperature:", temperature)
```

## Documentation of Main Modules and Classes

### makeblock.boards

The `makeblock.boards` module provides support for various Makeblock boards, including:

- `Halocode`
- `MegaPi`
- `mCore`
- `MeAuriga`
- `Neuron`
- `MegaPiPro`
- `MeOrion`
- `mBuild`
- `Codey`
- `CyberPi`
- `RJ25N`

### makeblock.comm

The `makeblock.comm` module provides communication interfaces for Makeblock devices, including:

- `SerialPort`
- `mlink`

### makeblock.modules

The `makeblock.modules` module provides support for various Makeblock modules, including:

- `RGBLed`
- `Speaker`
- `LedMatrix`
- `IrRemote`
- `Rocky`
- `Gamepad`
- `Gyro`
- `Power`
- `Potentiometer`
- `Sound`
- `Ultrasonic`
- `Button`
- `Slider`
- `Joystick`
- `SoilMoisture`
- `LaserRanging`
- `Flame`
- `Touch`
- `Light`
- `PIRMotion`
- `Magnetic`
- `Angle`
- `Motion`
- `Servo`
- `DCMotor`
- `EncoderMotor`
- `Color`
- `GPIO`
- `PowerManager`
- `Infrarer`
- `Temperature`
- `Humiture`
- `ExtDCMotor`
- `SmartServo`

## Examples Directory

The `examples` directory contains various examples for each supported board. These examples demonstrate how to use the Makeblock library to interact with different boards and modules.

### Available Examples

- `halocode`: Examples for the Halocode board.
- `megapi`: Examples for the MegaPi board.
- `mcore`: Examples for the mCore board.
- `meauriga`: Examples for the MeAuriga board.
- `neuron`: Examples for the Neuron board.
- `megapipro`: Examples for the MegaPiPro board.
- `meorion`: Examples for the MeOrion board.
- `mbuild`: Examples for the mBuild board.
- `codey`: Examples for the Codey board.
- `cyberpi`: Examples for the CyberPi board.
- `rj25n`: Examples for the RJ25N board.

### Navigating the Examples

To navigate to the `examples` directory and find examples for each supported board, follow these steps:

1. Open the `examples` directory.
2. Inside the `examples` directory, you will find subdirectories for each supported board (e.g., `halocode`, `megapi`, `mcore`, etc.).
3. Open the subdirectory corresponding to the board you are using.
4. Inside the subdirectory, you will find various example scripts demonstrating how to use the Makeblock library with that board.
