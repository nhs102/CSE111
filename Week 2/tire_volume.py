import math

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.

with open("volumes.txt", "at") as vol_file:

    current_date_and_time = datetime.now()

    width = int(input('Enter the width of the tire in mm (ex 205): '))

    ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))    

    diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    The_approximate_volume = math.pi * width ** 2 * ratio * (width * ratio + (2540 * diameter))/10000000000

    print(f"{current_date_and_time}, {width}, {ratio}, {diameter}, {The_approximate_volume:}", file=vol_file)

print(f"The approximate volume is {The_approximate_volume:.2f} liters.")
