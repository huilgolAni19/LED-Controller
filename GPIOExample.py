#!/usr/bin/env python3
import tkinter
import RPi.GPIO as gpio
from tkinter import *

class Application():

    def __init__(self):
       self.isLedOn=False
       self.buttonLed = None
       self.configureGPIO()
       self.createInterface()

    def createInterface(self):
       top = tkinter.Tk()
       top.title("LED Controller Example")
       top.geometry("300x200")
       self.buttonLed = Button(top, text="On Led", command = self.toggleButton, height=30, width=100)
       self.buttonLed.pack()
       top.bind("<Destroy>", self.closing)
       top.mainloop()


    def toggleButton(self):
        self.isLedOn = not self.isLedOn
        if self.isLedOn == True:
           print("Led is on")
           gpio.output(8, True)
           self.buttonLed["text"]= "Off Led"
        else:
           print("Led is off")
           gpio.output(8, False)
           self.buttonLed["text"]= "On Led"

    def configureGPIO(self):
        gpio.setmode(gpio.BOARD)  #Uses Pin Like on the board
        gpio.setup(8, gpio.OUT)   # pin no 8 Output

    def closing(self, event):
        print("Cleaning GPIO Config")
        gpio.cleanup()

if __name__ == "__main__":
    app = Application()
