# EMAN Software Overview

The EMAN software is written in Python and runs on a Raspberry Pi. It handles sensor initialization, data collection, logging, and future expansion into database storage and UI visualization.

## Modules

### sensors.py
Handles:
- BMH280 (I2C)
- ENS160 (I2C)
- SCD41 (I2C)
- PMS5003 (UART)


### main.py
Handles:
- System initialization
- Sensor polling
- Data logging
- Error handling
- Future database integration

## Python Requirement

# Index
- bh1750.py — I²C light sensor driver  
- eman_bme280.py — BME280 temperature/humidity/pressure driver  
- ds187b20.py — DS18B20 1‑Wire temperature probe driver  
- soil.py — Soil probe reading via MCP3008  
- relay.py — Relay control module  
- logger.py — Logging utility  
- main.py — Main program loop  
- test_mcp3008.py — ADC test script  
- config.py — Global configuration values
- bh1750_test.py — standalone test script for BH1750 light sensor
- light_log.csv — real logged data from the test run


