#type: ignore
import time
import board
import busio
import adafruit_gps 
 
import adafruit_mpu6050 

uart = busio.UART(tx=board.GP4, rx=board.GP5, baudrate=9600, timeout=10)

gps = adafruit_gps.GPS(uart, debug=False) 
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
sda_pin=board.GP14
scl_pin=board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
print(mpu.acceleration )


last_print = time.monotonic() 

while True:
    gps.update()
    current = time.monotonic() 
    print (mpu.acceleration)
    if mpu.acceleration[0] > 36:
        if current - last_print >= 1.0:
        last_print = current 
        print (mpu.acceleration[0])
        time.sleep(1)
    if mpu.acceleration[0] < -36:
        print (mpu.acceleration[0])
        time.sleep(1)
    if mpu.acceleration[1] > 36:
        print (mpu.acceleration[0])
        time.sleep(1)
    if mpu.acceleration[1] < -36:
        print (mpu.acceleration[0])
        time.sleep(1)
    if not gps.has_fix:
        # Try again if we don't have a fix yet.
        print("Waiting for fix...")
        continue