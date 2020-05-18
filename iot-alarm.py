import pifacecad
import datetime
import serial
import csv
import os

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
one0 = pifacecad.LCDBitmap([0b00001,0b00011,0b00111,0b01111,0b01101,0b01001,0b00001,0b00001])
one1 = pifacecad.LCDBitmap([0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b10000])
one2 = pifacecad.LCDBitmap([0b00001,0b00001,0b00001,0b00001,0b00001,0b01111,0b01111,0b01111])
one3 = pifacecad.LCDBitmap([0b10000,0b10000,0b10000,0b10000,0b10000,0b11110,0b11110,0b11110])

# the bit map for the number 2 in binary
two0 = pifacecad.LCDBitmap([0b00111,0b01111,0b01111,0b01100,0b00000,0b00000,0b00000,0b00000])
two1 = pifacecad.LCDBitmap([0b11000,0b11100,0b11110,0b01110,0b01110,0b01110,0b01110,0b11100])
two2 = pifacecad.LCDBitmap([0b00000,0b00001,0b00011,0b00111,0b00111,0b01111,0b01111,0b01111])
two3 = pifacecad.LCDBitmap([0b11000,0b10000,0b00000,0b00000,0b00000,0b11110,0b11110,0b11110])

# the bit map for the number 3 in binary
three0 = pifacecad.LCDBitmap([0b00011,0b00111,0b00111,0b00100,0b00000,0b00000,0b00000,0b00011])
three1 = pifacecad.LCDBitmap([0b11000,0b11100,0b11110,0b01110,0b01110,0b01110,0b11100,0b11000])
three2 = pifacecad.LCDBitmap([0b00011,0b00000,0b00000,0b00000,0b00100,0b01111,0b01111,0b00111])
three3 = pifacecad.LCDBitmap([0b11100,0b01110,0b01110,0b01110,0b01110,0b11100,0b11100,0b11000])

# the bit map for the number 4 in binary
four0 = pifacecad.LCDBitmap([0b00000,0b00000,0b00001,0b00001,0b00011,0b00011,0b00110,0b00110])
four1 = pifacecad.LCDBitmap([0b11100,0b11100,0b11100,0b11100,0b11100,0b11100,0b11100,0b11100])
four2 = pifacecad.LCDBitmap([0b01100,0b11100,0b11111,0b11111,0b00000,0b00000,0b00000,0b00000])
four3 = pifacecad.LCDBitmap([0b11100,0b11100,0b11111,0b11111,0b11100,0b11100,0b11100,0b11100])

# the bit map for the number 5 in binary
five0 = pifacecad.LCDBitmap([0b01111,0b01111,0b01110,0b01110,0b01110,0b01110,0b01111,0b01111])
five1 = pifacecad.LCDBitmap([0b11100,0b11100,0b11100,0b00000,0b00000,0b00000,0b11000,0b11100])
five2 = pifacecad.LCDBitmap([0b00000,0b00000,0b00000,0b00000,0b01000,0b01111,0b01111,0b00111])
five3 = pifacecad.LCDBitmap([0b11110,0b01110,0b01110,0b01110,0b01110,0b11100,0b11000,0b10000])

# storing the bitmaps to LCD memory
cad.lcd.store_custom_bitmap(0, one0)
cad.lcd.store_custom_bitmap(1, one1)
cad.lcd.store_custom_bitmap(2, one2)
cad.lcd.store_custom_bitmap(3, one3)

cad.lcd.store_custom_bitmap(4, two0)
cad.lcd.store_custom_bitmap(5, two1)
cad.lcd.store_custom_bitmap(6, two2)
cad.lcd.store_custom_bitmap(7, two3)

cad.lcd.store_custom_bitmap(8, three0)
cad.lcd.store_custom_bitmap(9, three1)
cad.lcd.store_custom_bitmap(10, three2)
cad.lcd.store_custom_bitmap(11, three3)

cad.lcd.store_custom_bitmap(12, four0)
cad.lcd.store_custom_bitmap(13, four1)
cad.lcd.store_custom_bitmap(14, four2)
cad.lcd.store_custom_bitmap(15, four3)

cad.lcd.store_custom_bitmap(16, five0)
cad.lcd.store_custom_bitmap(17, five1)
cad.lcd.store_custom_bitmap(18, five2)
cad.lcd.store_custom_bitmap(19, five3)

#time_alarm_test = datetime.strptime('%s %s'%(current_date, time_input),"%Y/%m/%d  %H:%M:%S")

while (count > 0):
        cad.lcd.home()
        date = datetime.now()
        cad.lcd.cursor_on()
#	cad.lcd.set_cursor(5,0)
#	cad.lcd.write(date.strftime("%H:%M"))
#	cad.lcd.set_cursor(0,2)
#	cad.lcd.write(date.strftime("%a %-d %b %Y"))
#	cad.lcd.cursor_off()
	
	# draw number 1
        cad.lcd.write_custom_bitmap(0)
        cad.lcd.write_custom_bitmap(1)
        cad.lcd.set_cursor(0,1)
        cad.lcd.write_custom_bitmap(2)
        cad.lcd.write_custom_bitmap(3)
	# draw number 2
        cad.lcd.set_cursor(2,0)
        cad.lcd.write_custom_bitmap(4)
        cad.lcd.write_custom_bitmap(5)
        cad.lcd.set_cursor(2,1)
        cad.lcd.write_custom_bitmap(6)
        cad.lcd.write_custom_bitmap(7)
	# draw number 3
	cad.lcd.set_cursor(4,0)
        cad.lcd.write_custom_bitmap(8)
        cad.lcd.write_custom_bitmap(9)
        cad.lcd.set_cursor(4,1)
        cad.lcd.write_custom_bitmap(10)
        cad.lcd.write_custom_bitmap(11)

	# draw number 4
	cad.lcd.set_cursor(6,0)
        cad.lcd.write_custom_bitmap(12)
        cad.lcd.write_custom_bitmap(13)
        cad.lcd.set_cursor(6,1)
        cad.lcd.write_custom_bitmap(14)
        cad.lcd.write_custom_bitmap(15)
	

	# draw number 5
	cad.lcd.set_cursor(8,0)
        cad.lcd.write_custom_bitmap(16)
        cad.lcd.write_custom_bitmap(17)
        cad.lcd.set_cursor(8,1)
        cad.lcd.write_custom_bitmap(18)
        cad.lcd.write_custom_bitmap(19)
	
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
        
