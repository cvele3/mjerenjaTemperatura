import nidaqmx as ni
import matplotlib.pyplot as plt
import numpy as np
from enum import Enum
import time


# Create a Task object
task = ni.Task()

# Add an input channel for voltage measurement
task.ai_channels.add_ai_voltage_chan("cDAQ9185-1F56937Mod1/ai0", min_val=-0.125, max_val=0.125)

# Start the measurement
while True:
    # Measure the voltage
    task.start()
    voltage = task.read()

    # Print the result
    print("Voltage value: ", voltage, "V")
    task.stop()
    #create delay
    #time.sleep(1)

# Delete the Task object
task.close()
