#code for MAX30100

import Adafruit_MAX30100

# Create a MAX30100 instance
mx30 = Adafruit_MAX30100.MAX30100()

# Function to read oxygen level and pulse rate data from the sensor
def read_max30100():
    mx30.begin()
    oxygen, pulse = mx30.read_sensor()
    return oxygen, pulse
