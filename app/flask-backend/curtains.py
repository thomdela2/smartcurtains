# Importeer de SenseHat
from sense_hat import SenseHat
import time

# Initailiseer
s = SenseHat()

# Toon bericht
white = (255,255,255)
nothing = (0,0,0)

def first_first():
	w = white
	o = nothing
	curtain_one = [
		w, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o, 
	]
	return curtain_one

def first_second():
	w = white
	o = nothing
	curtain_one = [
		o, w, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o,
		o, o, o, o, o, o, o, 
	]
	return curtain_one

curtain = [first_first]
count = 0

while True: 
	s.set_pixels(first_first)
    time.sleep(.75)
    count += 1