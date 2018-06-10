from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution=(2592,1944)
#camera.annotate_text="Harsh The Great"
#camera.brightness=70#default brightness is 50
#we can set the resolution manually max is (2592,1944) an least is (64,64)
#although by default it changes as per the screen resolution

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect=effect
    camera.annotate_text="effect: %s" % effect
    sleep(5)
#    camera.capture('/home/pi/Desktop/effects/type%s.jpg' % effect)
camera.stop_preview()
