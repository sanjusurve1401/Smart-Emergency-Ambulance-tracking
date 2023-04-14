#code for heart beat- XD-58C

from gpiozero import Button
from signal import pause

# Set up a Button instance for the XD-58C sensor module
xd58c = Button(21)

# Function to read data from the XD-58C sensor module
def read_xd58c():
    count = 0
    # Define a function to increment the count on each rising edge detected by the sensor
    def increment_count():
        nonlocal count
        count += 1
    # Attach the increment_count function to the rising_edge event of the sensor
    xd58c.when_pressed = increment_count
    # Wait for a short time to allow the sensor to detect heartbeats
    pause(0.5)
    # Detach the increment_count function from the sensor to stop detecting heartbeats
    xd58c.when_pressed = None
    # Return the number of heartbeats counted
    return count
