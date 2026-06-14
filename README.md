# DWDC — Double Wobble Drone

**DWDC (Double Wobble Drone Controller)** is an open-source budget drone project that includes:

- Semi-Complete drone-side code
- Serial monitor to arduino controller code
- 3D printable files for the drone frame and mounting parts
- (almost) All required design files to build the project from scratch

The goal of this project is to provide a simple and affordable drone platform that anyone can build at home using commonly available components.

---

## Required Parts

## Arduino Drone (DW) 

| Quantity | Part |
|--------:|------|
| 1x | Arduino Nano |
| 1x | 3S LiPo battery (any size that fits the frame) |
| 2x | 30A ESC (Electronic Speed Controller) |
| 2x | BLDC motors (2200KV or lower, must be the A2212 lineup) |
| 2x | SG90 9g servo motors |
| 1x | NRF24L01 wireless transceiver (PA + LNA version with antenna optional but not recommended) |
| 1x | I2C gyroscope/IMU (needed for stabalization ( and real-time simulation program coming later ;D )) |

### Notes

- If you use the PA + LNA version of the NRF24L01, the required antenna hole is already included in the drone body 3d file (might or might not fit, dunno yet).
- well made cable management is needed, or else face the hell of debugging the drone without knowing you are the problem.
- add capacitors to nrf module and ensure a 3.3v power supply is added to it as it isnt included in the parts, notice that some versions of the nrf are 5v capable but not clear.

---

## Controller

| Quantity | Part |
|--------:|------|
| 1x | a computer (phone serial monitor emulation coming in later versions) |
| 1x | Any microcontroller with exposed SPI pins, arduino uno recommended: 3.3v stable supply + Ease of adding extra features |
| 1x | NRF24L01 wireless transceiver (PA + LNA optional, still not recommended: can cause issues if drone gets out of line of sight of antenna) |

## ESP-NOW Capable Drone (ENDW)
| Quantity | Part |
|--------:|------|
| 2x | ESP32 (or any ESP-NOW capable board) |
| 1x | 3S LiPo battery (any size that fits the frame) |
| 2x | 30A ESC (Electronic Speed Controller) |
| 2x | BLDC motors (2200KV or lower, must be the A2212 lineup) |
| 2x | SG90 9g servo motors |
| 1x | I2C gyroscope/IMU (needed for stabalization and real-time simulation program ) |

### Notes

- Controller side ESP32 is included in the drone parts
- signal interference sucks, just manage your cables man
- capacitors are recommended (47uF 6V+) but not needed

### Optional

- A custom 3D-printed shield or enclosure can be designed to mount the microcontroller and radio to your controller.
- If you create a good case that might be cheaper to print or doesnt need printing, consider uploading it

---

## Features

- Low-cost design using world-wide hobby components (price for me came out to 76 dollars after taxes and printing
- Stabilization support through an I2C gyroscope/IMU
- Fully 3D-printable structure

---

## Project Goal

The purpose of DWDC is to make drone building accessible to hobbyists, students, and makers without breaking the bank on some 500 dollar drone that doesnt even come with a controller.

---

## License and Usage

These files are provided for **personal and educational use only**.

> **Commercial use is strictly prohibited without prior written permission from the author.**

If you wish to use any part of this project commercially, contact me, MO-D, for permission

---

## Contributing

- Suggestions, improvements, and custom 3D designs are welcome. If you develop better parts, enclosures, or software enhancements, consider sharing them so others can benefit.
- Donations will soon be up but you dont really need to donate, donating helps me bring out more designs, open source software AND hardware
- Discord link: https://discord.gg/kGYJnFMWCF

---

## AI Usage

AI was not, and will not be used, on this project. Any submissions that include fully AI generated content that has no prior human alterations and inspections will not be **ALLOWED**.
