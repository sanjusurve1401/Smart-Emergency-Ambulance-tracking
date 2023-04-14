# code for Function to read data from the LM-35 temperature sensor:
import gpiozero

# Create a LM35 instance
temp_sensor = gpiozero.MCP3008(channel=0)

# Function to read temperature data from the sensor
def read_temp():
    temp = temp_sensor.value * 330
    return temp
