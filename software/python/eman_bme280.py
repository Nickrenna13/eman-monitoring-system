# EMAN Environmental Monitoring System
# Module: BME280 - Temperture, humidity, pressure driver 
# Author: Nick
# Raspberry Pi Embedded Project

import time
import board
import busio
from adafruit_bme280.basic import Adafruit_BME280_I2C

# Initialize I2c
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize bme280
bme280 = Adafruit_BME280_I2C(i2c, address=0x76)

# Sea level pressure for altitube calculations
bme280.sea_level_pressure = 1013.25

while True:
	print("------BME280 Reading------")
	print(f"Temperature: {bme280.temperature:.2f} C")
	print(f"Humidity: {bme280.humidity:.2f} %")
	print(f"Pressure: {bme280.pressure:.2f} hPa")
	print("-------------------------------------------\n")
	time.sleep(2)
