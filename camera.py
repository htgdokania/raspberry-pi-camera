import cv2
from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution=(2592,1944)
#camera.annotate_text="Harsh The Great"
#camera.brightness=70#default brightness is 50
#we can set the resolution manually max is (2592,1944) an least is (64,64)
#although by default it changes as per the screen resolution

camera.start_preview()
#while True :
for i in range(1,100):
   	sleep(.1)
    	camera.annotate_text="brightness=%s" % i
       	camera.brightness=i
#	if cv2.waitKey(25) & 0xFF==ord('q'):
#		break
#
camera.capture('/home/pi/Desktop/brightness/level%s.jpg' % i)
camera.stop_preview()
