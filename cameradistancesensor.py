from picamera import PiCamera
import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
trig=20
echo=21
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig,1)
time.sleep(0.0001)
GPIO.output(trig,0)

while GPIO.input(echo)==0:
	start=time.time()
while GPIO.input(echo)==1:
	end=time.time()
ttime=end-start

#cm:
distance=ttime/0.000058

print(distance) 


camera=PiCamera()
camera.resolution=(2592,1944)
camera.annotate_text="Harsh The Great"
camera.annotate_text_size=100

camera.start_preview()

if distance<20:    
        camera.brightness=100
        time.sleep(5)
elif distance<50:
        camera.brightness=70
        time.sleep(5)
elif distance<100:
        camera.brightness=50
        time.sleep(5)
else:
        camera.brightness=30
        time.sleep(5)
camera.stop_preview()
GPIO.cleanup()
