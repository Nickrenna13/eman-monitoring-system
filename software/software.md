# EMAN Software Overview

The EMAN software is written in Python and runs on a Raspberry Pi. It handles sensor initialization, data collection, logging, and future expansion into database storage and UI visualization.

## Modules

### sensors.py
Handles:
- BME280 (I²C)
- BH1750 (I²C)
- DS18B20 (1‑Wire)

### adc.py
Handles:
- MCP3008 SPI ADC
- Reads 4 analog probe channels

### main.py
Handles:
- System initialization
- Sensor polling
- Data logging
- Error handling
- Future database integration

## Python Requirements

Install using:

