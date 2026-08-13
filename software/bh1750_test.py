########################################################################
# EMAN Environmental Monitoring System
# Module: Full Demo test with sensor BH1750 (light, I^2C) and a logging to csv file
# Author: Nick R
# Raspberry Pi Embedded Project
#########################################################################
# Notes: Reads lux then prints it. Saves it to light_log.csv, waits for
# 60 seconds but repeats forever or until program gracefully shuts down.
# This BH1750 is a test to show know-how and supports a real data logger

import RPi. GPIO as GPIO
import smbus2
import time
from datetime import datetime 

DEVICE = 0x23 # BH1750 default address
bus = smbus2.SMBus(1)
CONT_HIRES_MODE = 0x10

# initialize the relay
GPIO.setmode(GPIO.BCM)
RELAY_PIN = 17
GPIO.setup(RELAY_PIN, GPIO.OUT)

# BH1750 command for high-resolution continuous mode 
CONT_HIRES_MODE = 0x10

def read_light():
	#Send measurement command 
	bus.write_byte(DEVICE, CONT_HIRES_MODE)
	time.sleep(0.2) # Wait for mesurement 
	
	# Read two bytes of data
	data = bus.read_i2c_block_data(DEVICE, 0x00, 2)
	raw = (data[0] << 8) | data[1]

	# Convert to lux
	lux = raw / 1.2
	return lux
while True:
	lux = read_light()
	timestamp = datetime.now().isoformat()
	
	print(f"Light Level: {lux:.2f} lux")
	
	with open("light_log.csv", "a") as f:
		f.write(f"{timestamp},{lux:.2f}\n")
		
	# Automation logic
	LOW_LIGHT = 50 # lux threshold 
	if lux < LOW_LIGHT:
		GPIO.output(RELAY_PIN, GPIO.HIGH) # ex: turn grow light OH
	else:
		GPIO.output(RELAY_PIN, GPIO.LOW) # ex: turns grow light OFF
	
	
	time.sleep(60)
