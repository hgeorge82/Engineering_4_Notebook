#type: ignore
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

def triangle_area(val1, val2,val3):   

    try:
        val1 = val1.split(",")
        val2 = val2.split(",")
        val3 = val3.split(",")

        x1 = float(val1[0])
        y1 = float(val1[1])
        x2 = float(val2[0])
        y2 = float(val2[1])
        x3 = float(val3[0])
        y3 = float(val3[1])

        print(val1)
        print(val2)
        print(val3)
        
        hline = Line(x1,y1,x2,y2, color=0xFFFF00)
        splash.append(hline)
        
        circle = Circle(x, y, r, outline=0xFFFF00)
        splash.append(circle)
        
        triangle = Triangle(x1, y1, x2, y2, x3, y3, outline=0xFFFF00)
        splash.append(triangle)

        area = (abs(x1*(y2 - y3)+x2*(y3 - y1)+x3*(y1 - y2)))/2
        print(x1,y1,x2,y2,x3,y3)
        
        
        return area

    except:
        
        print("An exception occurred")
        area = 0 
        return area
      

while  True:
    val1 = input("Put coordinates in: ") 
    val2 = input("Put coordinates in: ")
    val3 = input("Put coordinates in: ")
    
    area = triangle_area(val1, val2, val3)
    
    if area == 0:
        continue
    else:
        print("The area of the triangle with vertices: ")
        print(area)
        