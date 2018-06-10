from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.resolution=(2592,1944)
camera.annotate_text="Harsh The Great"
camera.annotate_text_size=100 #valid size are 6 to 160 default 32
camera.brightness=70 #default brightness is 50
#we can set the resolution manually max is (2592,1944) an least is (64,64)
#although by default it changes as per the screen resolution

camera.start_preview()
#for i in range(100):
sleep(5)
    #camera.annotate_text="brightness=%s" % i
    #camera.brightness=i
camera.capture('/home/pi/Desktop/bigtext.jpg' )
camera.stop_preview()
