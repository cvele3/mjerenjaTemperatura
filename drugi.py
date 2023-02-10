import nidaqmx
import time
import nidaqmx.constants as constants
import nidaqmx.system as system

print(constants.TerminalConfiguration.RSE.value)


device = "cDAQ9185-1F56937Mod1"
channel = "ai0"

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan(device + "/" + channel)
    task.start()

    while True:
        voltage = task.read()
        print("Voltage: " + str(voltage))
        time.sleep(0.5)