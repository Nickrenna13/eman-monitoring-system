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
