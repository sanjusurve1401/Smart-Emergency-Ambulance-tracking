# code for ECG sensor
import ADS1x15

# Create an ADS1115 instance
adc = ADS1x15.ADS1115()

# Function to read ECG data from the sensor
def read_ecg():
    ecg = adc.read_adc(0, gain=1)
    return ecg
