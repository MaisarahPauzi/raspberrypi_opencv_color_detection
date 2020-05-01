from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2
from gpiozero import LED

led1 = LED(17)
led2 = LED(18)
led3 = LED(27)
led4 = LED(22)
led5 = LED(25)
led6 = LED(12)
led7 = LED(13)
led8 = LED(19)

def nothing(x):
    pass

def lightOn():
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    led5.on()
    led6.on()
    led7.on()
    led8.on()
    time.sleep(1)
    

def lightOff():
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    led5.off()
    led6.off()
    led7.off()
    led8.off()
    time.sleep(1)



camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640,480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    
    lowerLimit = np.array([0, 164, 64])
    upperLimit = np.array([107, 255, 255])
    
    mask = cv2.inRange(hsv, lowerLimit, upperLimit)
    
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # red color detected
    red_detected = cv2.countNonZero(mask)
    if red_detected > 20000:
        lightOn()
    else:
        lightOff()
    
    cv2.imshow("Original view", image)
    cv2.imshow("Mask", mask)
    
    key = cv2.waitKey(1) & 0xFF
    
    rawCapture.truncate(0)
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()
exit()
