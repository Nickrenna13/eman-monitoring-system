# EMAN Environmental Monitoring System
# Module: logger utility off a JSON
# Author: Nick
# Raspberry Pi Embedded Project

import json
import os

# Loads configureation values from config.json 
def load_config():
	# build the path the json
	base_path = os.path.dirname(os.path.dirname(__file__))
	config_path = os.path.join(base_path, "config", "config.json"0
	
	# Read and parse the JSON file
	with open(config_path, "r") as f:
		return json.load(f)
