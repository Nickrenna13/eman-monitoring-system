# PCB Overview
This PCB was designed in KiCad as part of the EMAN environmental monitoring system. Its purpose is to provide clean routing, stable power, and organized connectors for the Raspberry Pi and all sensors used in the project.

# Key Features
- Raspberry Pi 40‑pin header alignment
- I²C routing for BME280 and BH1750
- 1‑Wire routing for DS18B20
- SPI routing for MCP3008 ADC
- 4 analog probe connectors
- 3.3V and GND rails
- Silkscreen labels for easy wiring
- DRC cleanup and Gerber generation
# Design Goals
- Keep routing simple and beginner‑friendly
- Provide stable sensor connections
- Maintain clean ground reference
- Allow future expansion (relays, more sensors)
- Learn KiCad footprints, nets, and DRC rules
- ## Schematic Notes
- BME280 and BH1750 share the I²C bus (SDA/SCL)
- DS18B20 uses GPIO4 with a 4.7k pull‑up resistor
- MCP3008 uses SPI (CE0, MISO, MOSI, SCLK)
- All sensors use 3.3V logic
- Ground plane used for stability
## Layout Notes
- Clean routing for I²C and SPI
- Probe connectors placed on board edge
- Silkscreen labels for GPIO and sensor channels
- All DRC errors resolved
## Gerbers
Gerber files will be uploaded once fabrication is complete.
## Future Improvements
- Add mounting holes
- Add fuse or transient protection
- Add relay outputs
- Add external 5V regulator
- Add weatherproof enclosure connectors
