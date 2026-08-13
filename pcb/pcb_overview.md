# PCB Overview
This PCB was designed in KiCad as part of the EMAN environmental monitoring system. Its purpose is to provide clean routing, stable power, and organized connectors for the Raspberry Pi and all sensors used in the project.
<img width="850" height="550" alt="Screenshot 2026-08-06 092831" src="https://github.com/user-attachments/assets/c9b76055-1ba3-4c9f-8de7-9863c2c1cb7d" />


# Key Features
- Raspberry Pi 40‑pin header alignment
- I²C routing for BME280 and BH1750
- 1‑Wire routing for DS18B20
- SPI routing for MCP3008 ADC
- 4 analog probe connectors
- 3.3V and GND rails
- Silkscreen labels for easy wiring
- DRC cleanup and Gerber generation
<img width="800" height="400" alt="Screenshot 2026-08-06 091122" src="https://github.com/user-attachments/assets/a353e4bf-e579-4fb0-8814-825af03990a0" />

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
<img width="800" height="400" alt="Screenshot 2026-08-03 120422" src="https://github.com/user-attachments/assets/0b3914da-0ab8-4387-9a95-720cdd5688bd" />

## Layout Notes
- Clean routing for I²C and SPI
- Probe connectors placed on board edge
- Silkscreen labels for GPIO and sensor channels
- All DRC errors resolved
## Gerbers
Gerber files will be uploaded once fabrication is complete.
( Gerber files are uploaded as EMAN_gerbers.zip)
## Future Improvements
- Add fuse or transient protection
- Add relay outputs
- Add external 5V regulator
- Add weatherproof enclosure connectors
