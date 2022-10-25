#type: ignore
import board
import time
import digitalio
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', " ": "/"}

 
ledred = digitalio.DigitalInOut(board.GP16)
ledred.direction = digitalio.Direction.OUTPUT

 
 
while True:  
    mycar1 = input("Morse code translation: ")
    if mycar1 == "-q":
        break
    mycar1 = mycar1.upper()
    mileage1 = " "
for letter in mycar1:
    mileage1 = mileage1 + MORSE_CODE[letter] + " "
    print(mileage1)
    
for character in mycar1_message:
        if character == ".":
            ledred.value = True
            time.sleep(dot_time)
            ledred.value = False
            time.sleep(dot_time)
        
        if character == "-":
            ledred.value = True 
            time.sleep(dash_time)
            ledred.value = False
            time.sleep(dash_time)
            
        if character == " ":
            time.sleep(between_letters)
            
        if character == "/":
            time.sleep(between_words)
        