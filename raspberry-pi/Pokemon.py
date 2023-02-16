#type: ignore
import time
import board
import busio
import adafruit_gps 
 
import adafruit_mpu6050 
import storage 

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

x_acceleration = []
y_acceleration = []
z_acceleration = []
gps_altitude = []
gps_speed = []


while True:
    gps.update()
    current = time.monotonic() 
    print (mpu.acceleration)
    x_acceleration.append(mpu.acceleration[0])
    y_acceleration.append(mpu.acceleration[1])
    z_acceleration.append(mpu.acceleration[2])
    gps_altitude.append(gps.altitude_m)
    gps_speed.append(gps.speed_knots)
    #print(x_acceleration)
    time.sleep(1)
    if not gps.has_fix:
        # Try again if we don't have a fix yet.
        print("Waiting for fix...")
        continue
    if gps.altitude_m is not None:
            print("Altitude: {} meters".format(gps.altitude_m))
    if gps.speed_knots is not None:
            print("Speed: {} knots".format(gps.speed_knots))
            
        #print out datalease input valid coordinates (remember format x,y)") #u suck, fix it