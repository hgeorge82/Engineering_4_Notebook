# type: ignore
import time 
import board
import busio
import adafruit_mpl3115a2
import displayio



displayio.release_displays() 
sda_pin = board.GP10
scl_pin = board.GP11
i2c = busio.I2C(scl_pin, sda_pin)  



sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
#sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)


sensor.sealevel_pressure = 102250


while True:
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} pascals".format(pressure))
    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))
    temperature = sensor.temperature
    print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    time.sleep(1.0)