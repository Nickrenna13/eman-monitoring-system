# EMAN — Environmental Monitoring System
A microcontroller-based environmental monitoring and sensor integration project.

## Summary
EMAN is an embedded environmental monitoring system built around the ESP32 platform with multiple sensors and a touchscreen interface. This project demonstrates embedded firmware development, sensor integration, PCB design, and hardware prototyping.

## Hardware
- ESP32 Dev Board (V1 + touchscreen, V2)
- 2.8" LCD Touchscreen (SPI)
- Sensors:
  - PMS5003 (UART)
  - BME280 (I²C)
  - SCD41 (I²C)
  - ENS160+ (I²C)
- Custom PCB (KiCad)
- 12V power supply + regulation
- Connectors, wiring, standoffs, breadboard prototypes

## Software
- Embedded C (PlatformIO)
- VSCode
- Sensor drivers (UART + I²C)
- LCD UI rendering
- Modular firmware structure

## PCB Design
Located in `/pcb`  
Includes:
- Sensor connectors  
- Power routing  
- ESP32 header alignment  
- Silkscreen labeling  
- DRC cleanup  
- Gerber files  

## Photos
Located in `/photos`  
Includes:
- Hardware  
- Wiring  
- PCB  
- Assembly  

## Current Status
- Finalizing PCB routing  
- Integrating sensor drivers  
- Building touchscreen UI  
- Improving documentation  

## Future Plans
- Add database logging  
- Build visualization UI  
- Outdoor enclosure  
- Control outputs (relays, fans, pumps)  
- Multi-node sensor network  

