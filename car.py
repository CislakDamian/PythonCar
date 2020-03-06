import RPi.GPIO as gpio
import time
import readchar
from os import system

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(17, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)


def forward():
 init()
 # zolta strona 
 gpio.output(17, False) 
 gpio.output(22, True)
 # niebieslka strona
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(0.5)
 gpio.cleanup()

def back():
 init()
 # zolta strona 
 gpio.output(17, True) 
 gpio.output(22, False)
 # niebieslka strona
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(0.5)
 gpio.cleanup()

def turn_l():
 init()
 # zolta strona 
 gpio.output(17, True) 
 gpio.output(22, False)
 # niebieslka strona
 gpio.output(23, True) 
 gpio.output(24, False)
 time.sleep(0.5)
 gpio.cleanup()

def turn_r():
 init()
 # zolta strona 
 gpio.output(17, False) 
 gpio.output(22, True)
 # niebieslka strona
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(0.5)
 gpio.cleanup()

system ('clear')
print("-----------------------")
print("----- Car control -----")
print("-----------------------")
print("--                   --")
print("--   w - forward     --")
print("--   s - back        --")
print("--   d -turn right   --")
print("--   a - turn left   --")
print("--   e - exit        --")
print("--                   --")
print("-----------------------")
print("----- Log system ------")
print("-----------------------")

while(1):

    #x=raw_input()
    x=readchar.readchar()
    if x=='w':
        print("forward")
        forward()
        x='z'

    elif x=='s':
        print("back")
        back()
        x='z'

    elif x=='d':
        print("turn right")
        turn_r()
        x='z'

    elif x=='a':
        print("turn left")
        turn_l()
        x='z'
    
    elif x=='e':
	print("----------")
        print("Quit!")
        break
    
    else:
        print("<<<  WRONG input!  >>>")
        print("Please use wasd to control or e for exit...")
