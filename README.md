Environmental Monitoring System (EMAN)
A microcontroller-based environmental monitoring and sensor integration project.

Overview
EMAN is an embedded environmental monitoring system built around the ESP32 platform with optional touchscreen interfaces. The goal is to collect environmental data from multiple sensors, process it using Embedded C, and prepare the system for future expansion into control and automation applications.

This project is part of my transition into embedded systems, SBC-based control work, and prototype electronics.

Features
ESP32 (V1 + touchscreen, ESP32 V2)

2.8" LCD touchscreen interface (V1)

Multiple environmental sensors:

PMS5003 (UART)

BME280 (I²C)

SCD41 (I²C)

ENS160+ (I²C)

Custom PCB designed in KiCad (in progress)

Modular hardware layout for expansion

Documentation of wiring, design decisions, and testing

Hardware
ESP32 development boards (V1 + touchscreen, V2)

2.8" LCD screen (SPI)

Sensors:

PMS5003 (air particulate sensor)

BME280 (temperature, humidity, pressure)

SCD41 (CO₂)

ENS160+ (air quality VOC/NOx)

Custom PCB (KiCad) — routing in progress

Connectors, wiring, standoffs, resistors, barrel jacks

12V wall power supply with onboard regulation

Software
Embedded C

PlatformIO

Visual Studio Code

Sensor drivers (UART + I²C)

LCD display UI rendering

Planned data logging + modular firmware structure

PCB Design
The PCB is being created in KiCad and includes:

Sensor connectors (UART + I²C)

Power routing and regulation

ESP32 header alignment

Silkscreen labeling

DRC cleanup

Gerber generation

Screenshots and files will be available in /pcb.

Photos
Images of the hardware, wiring, PCB, and assembly process are located in /photos.

Status: In Progress
Current work:

Finalizing PCB routing and component placement

Integrating sensor drivers in PlatformIO

Building touchscreen UI elements

Improving documentation

Future Plans
Add database storage (SQLite or MongoDB) via external SBC or cloud endpoint

Build a small UI for data visualization

Add outdoor sensor enclosure

Integrate control outputs (relays, fans, pumps)

Expand to multi-node sensor network

This version fixes:

- V2 TouchScreen 

# About Me
I’m a hands-on worker/builder transitioning into embedded systems, SBC-based control work, and prototype electronics. EMAN is part of my portfolio demonstrating real-world embedded development.
