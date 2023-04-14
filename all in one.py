#all in one 

import Adafruit_MAX30100
import ADS1x15
import gpiozero
import RPi_I2C_driver

# Create a MAX30100 instance
mx30 = Adafruit_MAX30100.MAX30100()

# Create an ADS1115 instance
adc = ADS1x15.ADS1115()

# Create a LM35 instance
temp_sensor = gpiozero.MCP3008(channel=0)

# Create an LCD instance
lcd = RPi_I2C_driver.lcd()

# Function to read oxygen level and pulse rate from MAX30100 sensor
def read_max30100():
    mx30.begin()
    oxygen, pulse = mx30.read_sensor()
    return oxygen, pulse

# Function to read ECG data from ADS1115 sensor
def read_ads1115():
    ecg = adc.read_adc(0, gain=1)
    return ecg

# Function to read temperature data from LM35 sensor
def read_lm35():
    temp = temp_sensor.value * 330
    return temp

# Function to display sensor data on the LCD screen
def display_data():
    oxygen, pulse = read_max30100()
    ecg = read_ads1115()
    temp = read_lm35()
    lcd.lcd_display_string('Oxygen: %d%%' % oxygen, 1)
    lcd.lcd_display_string('Pulse: %d bpm' % pulse, 2)
    lcd.lcd_display_string('ECG: %d' % ecg, 3)
    lcd.lcd_display_string('Temp: %dC' % temp, 4)

# Call the display_data() function to display the sensor data on the LCD screen
display_data()
