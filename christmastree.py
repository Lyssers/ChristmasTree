import time
from threading import Thread
from sense_hat import SenseHat
from datetime import datetime
import sys
sense = SenseHat()
#sense.show_message("Merry Christmas!")
#sense.set_pixel(0,7,255,0,0)
#sense.load_image("pixil-frame-0.png")

X = (0,0,255)
O = (0,255,0)
B = (139,69,19)
Y = (255,255,0)
E = (0,0,0)

christmas_tree_with_red = [X,X,X,Y,Y,X,X,X,
                  X,X,X,O,O,X,X,X,
                  X,X,O,O,O,O,X,X,
                  X,O,O,O,O,O,O,X,
                  O,O,O,O,O,O,O,O,
                  X,O,O,O,O,O,O,X,
                  O,O,O,O,O,O,O,O,
                  X,X,X,B,B,X,X,X]

christmas_tree = [E,E,E,Y,Y,E,E,E,
                  E,E,E,O,O,E,E,E,
                  E,E,O,O,O,O,E,E,
                  E,O,O,O,O,O,O,E,
                  O,O,O,O,O,O,O,O,
                  E,O,O,O,O,O,O,E,
                  O,O,O,O,O,O,O,O,
                  E,E,E,B,B,E,E,E]
def LEDFunction():
    while True:
        sense.clear(0,0,255)
        time.sleep(0.5)
        sense.set_pixels(christmas_tree_with_red)
        time.sleep(0.5)
        sense.set_pixels(christmas_tree)
        time.sleep(0.5)
        sense.set_pixels(christmas_tree_with_red)
        time.sleep(0.5)
        sense.set_pixels(christmas_tree)
        time.sleep(0.5)
        sense.set_pixels(christmas_tree_with_red)
        time.sleep(0.5)
        sense.set_pixels(christmas_tree)
        time.sleep(0.5)
        sense.clear()
        sense.show_message("Happy 2019!",0.1,(255,255,255),(0,0,255))
        time.sleep(1)

def sensorFunction():
    measurementCounter = 0
    while True:
        measurementCounter =+ 1
        print ("Measurement number " + str(measurementCounter) + " since last program restart")
        print ("Current Time and Date of Measurement: " + str(datetime.now().strftime("%a %d of %b,%Y %X")))
        print ("Current humidity is: %s %%rH" % sense.get_humidity())
        print ("Current temperature is: %s C" % sense.get_temperature())
        print ("Current pressure is: %s Millibars" % sense.get_pressure())
        time.sleep(600)

if __name__ == "__main__":
    try:
        thread1 = Thread(target =  sensorFunction)
        thread2 = Thread(target = LEDFunction)
        thread1.daemon = True
        thread2.daemon = True
        thread1.start()
        thread2.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print (' Pressed, Goodbye...')
        sys.exit(0)