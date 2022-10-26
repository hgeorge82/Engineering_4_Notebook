#type: ignore
import board
import time
import digitalio
MORSE_CODE = { 'A':'.-', 'B':'-...',  #morse dictionary 
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

 
ledred = digitalio.DigitalInOut(board.GP16) #defining led pin
ledred.direction = digitalio.Direction.OUTPUT

modifier = 0.25  #morse code timing rules
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

 
while True:  
    mycar1 = input("Morse code translation: ") #Asking user for input
    if mycar1 == "-q": #a break that ends the code
        break
    mycar1 = mycar1.upper() # upper method(method that turns all lowercase letters uppercase)
    mileage1 = " " # where the morse letters are stored
for letter in mycar1: 
    mileage1 = mileage1 + MORSE_CODE[letter] + " " #calls for the translation to morse
    print(mileage1) 
    
for character in mycar1_message: #for whatever character you call the led blinks on and off 
        if character == ".": # added character
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
        