# EMAN Environmental Monitoring System
# Module: BH1750 Light Sensor
# Author: Nick
# Raspberry Pi Embedded Project

import smbus2
import time

class BH1750:
	DEVICE = 0X23
	ONE_TIME_HIGH_RES_MODE = 0x20

	def __init__(self, bus=1):
		self.bus = smbus2.SMBus(bus)

	def read(self):
		data = self.bus.read_i2c_block_data(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE, 2)
		return (data[0] << 8 | data[1]) / 1.2
