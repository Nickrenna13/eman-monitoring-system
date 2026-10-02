# Environmental Monitoring System (EMAN)
A Raspberry Pi–based environmental monitoring and sensor integration project.

# Overview
EMAN is an embedded environmental monitoring system built around a Raspberry Pi and a custom PCB designed in KiCad. The goal is to collect environmental data from multiple sensors, process it using Python, and prepare the system for future expansion into control applications.

This project is part of my transition into embedded systems, SBC-based control work, and prototype electronics.

# Features
- Raspberry Pi running embedded Linux

- Multiple environmental sensors (temperature, humidity, light, etc.)

- Custom PCB designed in KiCad

- Python scripts for sensor reading and data handling

- Modular hardware layout for future expansion

- Documentation of design decisions, wiring, and testing

# Hardware
- ESP32 V1, TouchScreen (2.8in) ESP32 V2.

- LCD screen V1

- Sensors (PMS5003 UART, BMH280 I2C, SCD41 I2C, ENS160+ I2C)

- Custom PCB (KiCad) -in progress

- Connectors, wiring, breadboard prototyping, standoffs, resistors, barrel jacks 

- Power supply considerations: 12V Wall



# Software
- Embedded C
- Platformio 
- VScode 


# PCB Design
The PCB was created in KiCad and includes:

- Sensor connectors

- Power routing

- Raspberry Pi header alignment

- Silkscreen labeling

- DRC cleanup

- Gerber generation

Screenshots and files are available in /pcb.

# Photos
Images of the hardware, wiring, PCB, and assembly process are located in /photos.

# Status: In Progress
Current work:

- Finalizing PCB assembly (components arriving soon)

- Expanding Python scripts

- Adding more sensors

- Improving documentation

# Future Plans
- Add database storage (SQLite or MongoDB)

- Build a small UI for data visualization

- Add outdoor sensor enclosure

- Integrate control outputs (relays, fans, pumps)

- V2 TouchScreen 

# About Me
I’m a hands-on worker/builder transitioning into embedded systems, SBC-based control work, and prototype electronics. EMAN is part of my portfolio demonstrating real-world embedded development.
