# EMAN Environmental Monitoring System
# Module: Main program loop 
# Author: Nick
# Raspberry Pi Embedded Project

import time
from sensors.bh1750 import BH1750
from sensors.bme280 import BME280Sensor
from sensors.ds18b20 import DS18B20
from sensors.soil import SoilSensor
from relay import Relay
from logger import setup_logger
from config import lead_config

def main():
	# Load config values (threshold relay pin, interval)
	cfg = load_config()
	#Initialize the logging system so all reading and errors go to here
	log = setup_logger()
	
	# Initialize sensors and hardware interfaces 
	bh = BH1750() 					# Light Sensor
	bme = BME280Sensor() 			# Temp Humidity Pressure (I^2C)
	ds = DS18B20() 					# Temp probe (1-Wire)
	soil = SoilSensor(pin=21) 		# apacitive soil mositure sensor (digital GPIO)
	
	# This is the main loop running like firmware aka continuously 
	while True:
		try:
			# Reading all sensor values 
			light = bh.read()
			env = bme.read()
			temp2 = ds.read()
			soil_val = soil.read() 
			
			# Log Sensor readings for debugging and/or analysis
			log.info(
				f"Light={light} lux | "
				f"Temp={env['temperature']}c | "
				f"Hum={env['humidity']}% | "
				f"Soil={soil_val}"
			)
			# Automation logic and relay turns ON if any threshold is exceeded
			if cfg["relay_mode" == "auto":
				# Light too low
				if light < cfg["light_threshold"]:
					relay.on()
				# Temp is too High
				if env["temperature"] > cfg["temp_threshold"]:
					relay.on()
				# Soil is too dry (1 = dry)
				if soil_val < cfg["soil_threshold"]:
					relay.on()
				# else turn off relay
				else:
					relay.off()
		except Exception as e:
			# logging error while keeping the system running
			log.error(f"Error: {e}")
		# waiting for the configured interval before next sensor read
		time.sleep(cfg["internal_seconds"])
# Entry point 
if __name__ = "__main__":
	main()
					
					
					
					
					
					
			
			
