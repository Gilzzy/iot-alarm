import pifacecad
import datetime
import serial
import csv
import os
import time

from datetime import datetime
import subprocess

#PiFaceCAD Setup
cad = pifacecad.PiFaceCAD()
cad.lcd.clear()
cad.lcd.backlight_on()
cad.lcd.blink_off()

#Global Variables
count = 1
backlight = 1
time_wake = str("06:30")
time_sleep = str("22:00")
#current_date = str("2019/02/18")

# the bit map for the number 1 in binary
LT = pifacecad.LCDBitmap([0B00111,0B01111,0B11111,0B11111,0B11111,0B11111,0B11111,0B11111])
UB = pifacecad.LCDBitmap([0B11111,0B11111,0B11111,0B00000,0B00000,0B00000,0B00000,0B00000])
RT = pifacecad.LCDBitmap([0B11100,0B11110,0B11111,0B11111,0B11111,0B11111,0B11111,0B11111])
LL = pifacecad.LCDBitmap([0B11111,0B11111,0B11111,0B11111,0B11111,0B11111,0B01111,0B00111])
LB = pifacecad.LCDBitmap([0B00000,0B00000,0B00000,0B00000,0B00000,0B11111,0B11111,0B11111])
LR = pifacecad.LCDBitmap([0B11111,0B11111,0B11111,0B11111,0B11111,0B11111,0B11110,0B11100])
MB = pifacecad.LCDBitmap([0B11111,0B11111,0B11111,0B00000,0B00000,0B00000,0B11111,0B11111])
block = pifacecad.LCDBitmap([0B11111,0B11111,0B11111,0B11111,0B11111,0B11111,0B11111,0B11111])

# storing the bitmaps to LCD memory
cad.lcd.store_custom_bitmap(0, LT)
cad.lcd.store_custom_bitmap(1, UB)
cad.lcd.store_custom_bitmap(2, RT)
cad.lcd.store_custom_bitmap(3, LL)
cad.lcd.store_custom_bitmap(4, LB)
cad.lcd.store_custom_bitmap(5, LR)
cad.lcd.store_custom_bitmap(6, MB)
cad.lcd.store_custom_bitmap(7, block)

#time_alarm_test = datetime.strptime('%s %s'%(current_date, time_input),"%Y/%m/%d  %H:%M:%S")

def display_0(x):
	cad.lcd.set_cursor(x,0)
	cad.lcd.write_custom_bitmap(0)
	cad.lcd.write_custom_bitmap(1)
	cad.lcd.write_custom_bitmap(2)
	cad.lcd.set_cursor(x,1)
	cad.lcd.write_custom_bitmap(3)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(5)
	
def display_1(x):
        cad.lcd.set_cursor(x,0)
        cad.lcd.write_custom_bitmap(1)
        cad.lcd.write_custom_bitmap(2)
        cad.lcd.write(" ")
        cad.lcd.set_cursor(x,1)
        cad.lcd.write_custom_bitmap(4)
        cad.lcd.write_custom_bitmap(7)
        cad.lcd.write_custom_bitmap(4)
	
def display_2(x):
	cad.lcd.set_cursor(x,0)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.write_custom_bitmap(2)
	cad.lcd.set_cursor(x,1)
	cad.lcd.write_custom_bitmap(3)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(4)
	
def display_3(x):
	cad.lcd.set_cursor(x,0)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.write_custom_bitmap(2)
	cad.lcd.set_cursor(x,1)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(5)
	
def display_4(x):
    cad.lcd.set_cursor(x,0)
    cad.lcd.write_custom_bitmap(3)
    cad.lcd.write_custom_bitmap(4)
    cad.lcd.write_custom_bitmap(7)
    cad.lcd.set_cursor(x,1)
    cad.lcd.write("  ")
    cad.lcd.write_custom_bitmap(7)
	
def display_5(x):
	cad.lcd.set_cursor(x,0)
	cad.lcd.write_custom_bitmap(3)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.set_cursor(x,1)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(5)

def display_6(x):
	cad.lcd.set_cursor(x,0)
	cad.lcd.write_custom_bitmap(0)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.set_cursor(x,1)
	cad.lcd.write_custom_bitmap(3)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(5)
	
def display_7(x):
    cad.lcd.set_cursor(x,0)
    cad.lcd.write_custom_bitmap(1)
    cad.lcd.write_custom_bitmap(1)
    cad.lcd.write_custom_bitmap(2)
    cad.lcd.set_cursor(x,1)
    cad.lcd.write("  ")
    cad.lcd.write_custom_bitmap(7)
	
def display_8(x):
	cad.lcd.set_cursor(x,0)
	cad.lcd.write_custom_bitmap(0)
	cad.lcd.write_custom_bitmap(6)
	cad.lcd.write_custom_bitmap(2)
	cad.lcd.set_cursor(x,1)
	cad.lcd.write_custom_bitmap(3)
	cad.lcd.write_custom_bitmap(4)
	cad.lcd.write_custom_bitmap(5)

def display_9(x):
    cad.lcd.set_cursor(x,0)
    cad.lcd.write_custom_bitmap(0)
    cad.lcd.write_custom_bitmap(6)
    cad.lcd.write_custom_bitmap(2)
    cad.lcd.set_cursor(x,1)
    cad.lcd.write("  ")
    cad.lcd.write_custom_bitmap(7)
	
def print_large_number(x_pos, number):
    switcher = {
            0: display_0,
            1: display_1,
            2: display_2,
	    3: display_3,
	    4: display_4,
            5: display_5,
            6: display_6,
            7: display_7,
	    8: display_8,
	    9: display_9,
            }

    func = switcher.get(number, "nothing")

    return func(x_pos)

while (count > 0):
        cad.lcd.home()
        date = datetime.now()
	
        cad.lcd.cursor_on()
        
        numbers = [0,1,2,3,4,5,6,7,8,9]
        for x in numbers:
            print_large_number(5,x)
            time.sleep(.5)
	
#	cad.lcd.set_cursor(5,0)
#	cad.lcd.write(date.strftime("%H:%M"))
#	cad.lcd.set_cursor(0,2)
#	cad.lcd.write(date.strftime("%a %-d %b %Y"))
#	cad.lcd.cursor_off()
	
#	print(time_alarm)
#	print(time_input)
#	print(date.strftime("%H:%M:%S"))

#	if backlight == 0:
#		if time_wake == date.strftime("%H:%M"):
#			cad.lcd.backlight_on()
#			backlight = 1
#	else :
#		if time_sleep == date.strftime("%H:%M"):
#			cad.lcd.backlight_off()
#			backlight = 0

#	if cad.switches[4].value:
#		if backlight == 1:
#			cad.lcd.backlight_off()
#			backlight = 0
#		else :
#			cad.lcd.backlight_on()
#			backlight = 1
#	time.sleep(.5)
        
