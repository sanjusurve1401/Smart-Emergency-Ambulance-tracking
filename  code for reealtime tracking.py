# code for reealtime tracking
import serial
import pynmea2
import time

# Set up the serial connection to the GSM/GPS module
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Function to get the real-time location from the GSM/GPS module
def get_location():
    # Send the command to get the GPS data
    ser.write(b'AT+CGNSINF\r\n')
    # Wait for a short time to allow the GPS module to respond
    time.sleep(0.5)
    # Read the response from the GPS module
    response = ser.readline().decode('utf-8')
    # Parse the GPS data using the pynmea2 library
    gps_data = pynmea2.parse(response)
    # Extract the latitude and longitude from the GPS data
    latitude = gps_data.latitude
    longitude = gps_data.longitude
    # Return the latitude and longitude as a tuple
    return (latitude, longitude)
