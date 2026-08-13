# EMAN Environmental Monitoring System
# Module: Relay testing script 
# Author: Nick
# Raspberry Pi Embedded Project

import RPi.GPIO as GPIO

class Relay:
	def __init__(self, pin):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin, GPIO.OUT)
		self.pin = pin
		
	def on(self):
		GPIO.output(self.pin, GPIO.HIGH)
		
	def off(self):
		GPIO.output(self.pin, GPIO.LOW)
