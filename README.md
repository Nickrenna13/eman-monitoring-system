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

#Hardware
- Raspberry Pi (model used)

- Sensors (DHT22, DS18B20, etc.)

- Custom PCB (KiCad)

- Connectors, wiring, and breadboard prototyping

- Power supply considerations

See the /hardware and /pcb folders for schematics, layout files, and design notes.

# Software
Python scripts handle:

- Sensor initialization

- Data reading

- Logging

- Basic error handling

- Future expansion for database storage

See the /software folder for code.

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

- Migrate to industrial SBC for long-term deployment

# About Me
I’m a hands-on technician transitioning into embedded systems, SBC-based control work, and prototype electronics. EMAN is part of my portfolio demonstrating real-world embedded development.
