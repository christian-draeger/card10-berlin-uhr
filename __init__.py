import utime
import leds

WIDTH = 160
HEIGHT = 80

CWIDTH = 13
CHEIGHT = 20

OUTER_COLOR = (180, 180, 180)
ltime = utime.localtime()
hours = ltime[3]
mins = ltime[4]

def display_hours():
	pass

def display_minutes():
	pass

def display_seconds():
	ltime = utime.localtime()
	secs = ltime[5]
	if secs % 2 == 0:
		# second value is brightness of led (0 - 31)
		leds.set_rocket(1, 31)
	else:
		leds.set_rocket(1, 0)

def main():
    while True:
    	display_seconds()

main()