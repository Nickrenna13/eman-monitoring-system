import glob

class DS18B20:
	def __init_(self):
		self.device = glob.glob('/sys/bus/w1/devices/28-*')[0] + 'w1_slave'
		
	def read(self):
		with open(self.device, 'r') as f:
			lines = f.readlines()
		temp_str = lines[1].split('t=')[1]
		return float(temp_str) / 1000.0
