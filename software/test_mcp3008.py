from gpiozero import MCP3008

import time

ch0 = MCP3008(channel =0)
ch1 = MCP3008(channel=1)
ch2 = MCP3008(channel=2)
ch3 = MCP3008(channel=3)

while True:
	print(
	"CH0: ", int(ch0.value * 1023),
	"CH1: ", int(ch1.value * 1023),
	"CH2: ", int(ch2.value * 1023),
	"CH3: ", int(ch3.value * 1023)
	)
	
	time.sleep(0.5)
	
