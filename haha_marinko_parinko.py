import nidaqmx
import Constants

device = "cDAQ9185-1F56937Mod1"
#device = "Dev1"
channel = "ai0"

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan(device + "/" + channel, terminal_config=Constants.TerminalConfiguration.RSE)
    data = task.read()
    print(data)
