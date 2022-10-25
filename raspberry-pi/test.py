#type: ignore
def triangle_area(x1y1, x2y2, x3y3)     

try:
    val1 = input("Put coordinates in: ") 
    val2 = input("Put coordinates in: ")
    val3 = input("Put coordinates in: ")

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
    
    area = (abs(x1*(y2 - y3)+x2*(y3 - y1)+x3*(y1 - y2)))/2
    print(x1,y1,x2,y2,x3,y3)
    
    
    return area

except:
    
      print("An exception occurred")
      

while  True:
    val1 = 
    val2 =
    val3 = 
    
    area = area_triangle(val1, val2, val3)
    
    if area == 0
    
    else: 
        print
