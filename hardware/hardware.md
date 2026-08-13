# Hardware Overview
# Sensors 
- BME280 - Temperature, Humidity, Pressure(I2C)
- DS18B20 - waterproof temperature probe (1-Wire)
- BH1750 - Ambient light measurement (I2C)
- Analog Probes vis MCP3008 (SPI ADC)
# Wiring 
## BME280 (I2C)
- VCC -> 3.3V
- GND -> Ground
- SDA -> Raspberry Pi SDA (GPIO2)
- SCL -> Raspberry Pi SCl (GPIO3)
## BH1750 (I2C)
- VCC -> 3.3V
- GND -> Ground
- SDA -> Raspberry Pi SDA (GPIO2)
- SCL -> Raspberry Pi SCL (GPIO3)
## DS18B20 (1‑Wire)
- VCC → 3.3V
- GND → Ground
- Data → GPIO4 (typical 1‑Wire pin)
- 4.7k resistor between Data and VCC
## MCP3008 (SPI)
- VDD → 3.3V
- VREF → 3.3V
- AGND → Ground
- DGND → Ground
- CLK → GPIO11 (SCLK)
- DOUT → GPIO9 (MISO)
- DIN → GPIO10 (MOSI)
- CS → GPIO8 (CE0)
- CH0–CH3 → Your 4 analog probes
# Power Notes
- Raspberry Pi powered via USB‑C or regulated 5V supply
- All sensors powered from Pi 3.3V rail
-MCP3008 uses 3.3V logic (safe for Pi)
- Total current draw is low (<200mA for sensors)
- PCB includes:
  - 3.3V rail routing
  - Ground plane
  - Pi header alignment
- Future improvements:
  - Add fuse or transient protection
  - Add outdoor-rated enclosure
  - Add dedicated 5V regulator for external loads
# Future Hardware Plans
- Add soil moisture sensors
- Add CO₂ sensor
- Add relay outputs for fans/pumps
- Add weatherproof enclosure
- Add cable strain relief and connector housings
- Migrate to industrial SBC for long-term deployment
