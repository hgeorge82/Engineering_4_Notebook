
#type: ignore
import time
import board
import busio

import adafruit_gps


uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)

gps = adafruit_gps.GPS(uart, debug=False)  
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")


last_print = time.monotonic()
Values=open(f"/data/{time.monotonic()}.csv","w")
while True:
    gps.update()
    current = time.monotonic() 

    #print(x_acceleration)
    time.sleep(1)
    if not gps.has_fix:
        # Try again if we don't have a fix yet.
        print("Waiting for fix...")
        continue
    gps_altitude.append(gps.altitude_m)
    gps_speed.append(gps.speed_knots)
    if gps.altitude_m is not None:
            print("Altitude: {} meters".format(gps.altitude_m))
    if gps.speed_knots is not None:
            print("Speed: {} knots".format(gps.speed_knots))
             Values.write(f"{gps.altitude_m},{gps.speed_knots}\n") # i changes every single
     break 
 
 '''       
Values=open(f"/data/{time.monotonic()}.csv","w")
for i in range(len(gps_altitude)): #gives number of items in list
    Values.write(f"{gps_altitude[i]},{gps_speed_knots[i]}\n") # i changes every single
Values.close    
'''