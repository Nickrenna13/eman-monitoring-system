# EMAN Environmental Monitoring System
# Module: Soil probe reading via MCP3008
# Author: Nick R
# Raspberry Pi Embedded Project

# 0 = went
# 1 = dry
import RPi.GPIO as GPIO

class SoilSensor:
	def __init__(self, pin):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin, GPIO.IN)
		self.pin = pin
	def read(self):
		return GPIO.input(self.pin)
