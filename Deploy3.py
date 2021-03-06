#import Temperature
import max30102
import hrcalc
import time
import os
import sys
import shutil
import draw
import cv2
import numpy as np
import detection
from detection import take_snap
from SafeThreads import *
from draw import *
from imutils.video.pivideostream import PiVideoStream

tempLow=95; tempHigh=99;
oxyLow=95; 

if __name__ == '__main__':
  
  
  cv2.namedWindow("SAFE Biosecurity Solutions", cv2.WND_PROP_FULLSCREEN)
  cv2.setWindowProperty("SAFE Biosecurity Solutions",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
  
  faceDetector=detection.Detector()
    
  
  while True:
    Display().run(start_screen())
    if len(faceDetector.detect_and_predict_mask(take_snap(), faceDetector.faceNet)) !=0:
      break
    else:
      print("waiting.....")
      time.sleep(0.3)
  while True:
    if 'entry.txt' not in os.listdir("/home/pi"):
      break
    else:
      Display().run(wait_screen())
      time.sleep(0.5)
  
  #check face mask
  mask=faceDetector.start(frames=3)
  time.sleep(1)
  
  
  if not mask:
    Display().run(no_mask_screen1(take_snap()))
    time.sleep(4)
    mask=faceDetector.start(frames=3)
    if not mask:
      Display().run(no_mask_screen2(),4)
      time.sleep(4)
      sys.exit("NO MASK")
    
  Display().run(temp_screen(),3)
  time.sleep(3)
    
  #check temperature
  '''
  temp_sensor = Temperature.MLX90614()
  tempVal=temp_sensor.get_avg_temp()'''
  tempVal=97.50
  time.sleep(3)
  if tempVal>tempHigh or tempVal<tempLow:
    Display().run(tempVal,no_temp_screen1(take_snap()),5)
    '''
    temp_sensor = Temperature.MLX90614()
    tempVal=temp_sensor.get_avg_temp()'''
    tempVal=97.50
    time.sleep(3)
    if tempVal>tempHigh or tempVal<tempLow:
      Display().run(no_temp_screen2(),3)
      time.sleep(3)
      sys.exit("TEMPERATURE")
    
  Display().run(edit_frame(take_snap(),True,tempVal,True),3)
  time.sleep(2)
  Display().run(oxy_screen(),2)
    
  
    
  #check oxygen
  '''
  while True:
    max_obj = max30102.MAX30102()
    red_data, ir_data = max_obj.read_sequential()
    time.sleep(1)
    hr, hrc, spo2, spo2c = hrcalc.calc_hr_and_spo2(ir_data[:100], red_data[:100])
    if True:
      break'''
  spo2=99
  time.sleep(3)
  if spo2<oxyLow:
    Display().run(no_oxy_screen1(tempVal,spo2,take_snap()),3)
    time.sleep(3)
    '''
    while True:
      Display().run(no_oxy_screen1(tempVal,spo2,take_snap()))
      max_obj = max30102.MAX30102()
      red_data, ir_data = max_obj.read_sequential()
      time.sleep(1)
      hr, hrc, spo2, spo2c = hrcalc.calc_hr_and_spo2(ir_data[:100], red_data[:100])
      if True:
        break'''
    spo2=99
    time.sleep(3)
    if spo2<oxyLow:
      Display().run(no_oxy_screen2())
      sys.exit("OXYGEN")
  Display().run(entry_screen(take_snap()),2)
  f=open("/home/pi/entry.txt",'+w')
  f.close()
  time.sleep(4)
'''   mask = faceDetector.start(tempVal,True,spo2,True,frames=10)
  time.sleep(1)
  if mask:
    Display().run(entry_screen(take_snap()),2)
    f=open("/home/pi/entry.txt",'+w')
    f.close()
    time.sleep(4)
  else:
    Display().run(no_mask_screen2(),2)
    time.sleep(2)'''
  
  while True:
    if 'exit.txt' in os.listdir("/home/pi"):
      os.remove("/home/pi/exit.txt")
      break
    else:
      Display().run(wait_screen())
      time.sleep(0.5)

  cv2.destroyAllWindows()

	
