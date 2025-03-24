# Makeblock Library

The Makeblock library is a Python package that provides an interface to interact with various Makeblock devices and modules. It includes support for different boards, communication protocols, and modules, allowing users to control and interact with Makeblock hardware using Python.

## Features

- Support for multiple Makeblock boards, including Halocode, MegaPi, mCore, MeAuriga, and more.
- Communication with Makeblock devices using SerialPort and mlink.
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
