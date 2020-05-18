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

# the bit map for the 4 characters that make up the tardis, in hex
tardis0 = pifacecad.LCDBitmap([0x1, 0x7, 0xF, 0xF, 0x9, 0x9, 0x9, 0xF])
tardis1 = pifacecad.LCDBitmap([0x10, 0x1c, 0x1e, 0x1e, 0x12, 0x12, 0x12, 0x1e])
tardis2 = pifacecad.LCDBitmap([0xf, 0x9, 0x9, 0x9, 0xf, 0xf, 0xf, 0x1f])
tardis3 = pifacecad.LCDBitmap([0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1e, 0x1f])

# storing the bitmaps to LCD memory
cad.lcd.store_custom_bitmap(0, tardis0)
cad.lcd.store_custom_bitmap(1, tardis1)
cad.lcd.store_custom_bitmap(2, tardis2)
cad.lcd.store_custom_bitmap(3, tardis3)


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
	
	# draw the tardis
        cad.lcd.write_custom_bitmap(0)
        cad.lcd.write_custom_bitmap(1)
        cad.lcd.set_cursor(0,1)
        cad.lcd.write_custom_bitmap(2)
        cad.lcd.write_custom_bitmap(3)


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
        
