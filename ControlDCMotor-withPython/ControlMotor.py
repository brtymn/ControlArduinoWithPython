## Control DC Motor With Python

from tkinter import *
import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(0.5)

def selection():
   selection1 = "You selected the Direction " + str(var1.get())
   l2.config(text = selection1)

def Level_one():
   if (var1.get() == 1):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '60 ' + '0' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)

   if (var1.get() == 2):
           arduino.flushInput()
           arduino.flushOutput()
           selection = 'PWM ' + '0 ' + '60' + '\r'
           arduino.write(selection.encode('utf-8'))
           print(selection)


def Level_two():
   if (var1.get() == 1):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '130 ' + '0' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)
   if (var1.get() == 2):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '0 ' + '130' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)


def Level_three():
   if (var1.get() == 1):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '190 ' + '0' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)
   if (var1.get() == 2):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '0 ' + '190' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)


def Level_four():
   if (var1.get() == 1):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '255 ' + '0' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)
   if (var1.get() == 2):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '0 ' + '255' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)


def pwm():
   if (var1.get() == 1):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + str(var2.get()) + ' 0' + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)
   if (var1.get() == 2):
       arduino.flushInput()
       arduino.flushOutput()
       selection = 'PWM ' + '0 ' + str(var2.get()) + '\r'
       arduino.write(selection.encode('utf-8'))
       print(selection)


def stop():
   arduino.flushInput()
   arduino.flushOutput()
   selection = 'PWM ' + '0' + ' 0' + '\r'
   arduino.write(selection.encode('utf-8'))
   print(selection)

root = Tk()
var1 = IntVar()
var2 = IntVar()
root.geometry('1000 x 800')
root.title("DC Motor Control")
R1 = Radiobutton(root, text = "Direction 1", variable = var1, value = 1, command = sel)
R2 = Radiobutton(root, text ="Direction 2", variable = var1, value = 2, command = sel)
l1 = Label(root, text ='DC Motor Controller')
l2 = Label(root, text ='Please Specify the Motor Direction')
b1 = Button(root, text = "Level One", command = Level_one)
b2 = Button(root, text = "Level Two", command = Level_two)
b3 = Button(root, text = "Level Three", command = Level_three)
b4 = Button(root, text = "Level Four", command = Level_four)
b5 = Button(root, text = "Stop", command = stop)
b6 = Button(root, text = "SEND PWM TO ARDUINO", command = pwm)
s1 = Scale(root, label = "Set PWM Value", orient = HORIZONTAL, from_= 0, to = 255, variable = var2, sliderlength = 20, length = 300)
s1.set(150)

l1.pack()
R1.pack()
R2.pack()
l2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
s1.pack()
b6.pack()

root.mainloop()
