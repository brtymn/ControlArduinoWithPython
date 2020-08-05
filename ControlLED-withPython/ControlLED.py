## Control LED With Python

from tkinter import *
import serial
import time
arduino =serial.Serial('/dev/ttyACM0', 9600)
time.sleep(0.5)
def RED_on():
   selection = 'LEDON\n\r'
   arduino.write(selection.encode('utf-8'))


def LED_off():
   time.sleep(0.1)
   selection ='OFF\n\r'
   arduino.write(selection.encode('utf-8'))
def REDP():
   time.sleep(0.1)
   selection= 'LEDPWM ' + str(var1.get()) + '\n\r'
   arduino.write(selection.encode('utf-8'))



root = Tk()
var1 = IntVar()
root.geometry()
root.title('LED Controller')
l1 = Label(root,text = 'Control Interface')
b1 = Button(root, text = 'LED ON', command = LED_on)
b4 = Button(root, text = 'LED OFF',command = LED_off)
b5 = Button(root, text = 'LED PWM',command = LEDPWM)

s1 = Scale(root, label = 'Set PWM',orient = HORIZONTAL,from_=0,to=255,variable = var1,sliderlength = 20,length = 300)
s1.set(150)
l1.grid(row=0, column=4)
b1.grid(row=1, column=4)
b4.grid(row=2, column=4)
b5.grid(row=3, column=4)
s1.grid(row=4, column=0, columnspan=9)
root.mainloop()
