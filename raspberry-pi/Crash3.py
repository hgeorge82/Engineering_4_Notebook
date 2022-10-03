#type: ignore
from adafruit_display_text import label
import adafruit_displayio_ssd1306 
import terminalio
import displayio
import board
import time
import busio

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=your-address-here, reset=board.your-pin-here)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=your-address-here)

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

# you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
# Don't forget to round the angular velocity values to three decimal places

# send display group to screen
display.show(splash)
