import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def title(frame):
       framec=frame.copy()
       cv2.rectangle(frame,(0,0),(1024,100),(50,50,50),-1)
       alpha = 0.3
       frame = cv2.addWeighted(framec, alpha, frame, 1 - alpha, 0)
       frame = cv2.putText(frame, 'S.A.F.E. Biosecurity Solutions', (160,60), 
                            cv2.FONT_HERSHEY_COMPLEX, 1.4, (255,255,255), 2, cv2.LINE_AA) 
       return frame
       
def create_frame(val=255):
       scrn=np.full((768,1024,3), 255, dtype=np.uint8)
       scrn=title(scrn)
       return scrn

def wait_screen(scrn=create_frame()):
       return cv2.putText(scrn, "The Booth is currently occupied, please await your turn.", (15,768//2 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) 
                            
def no_face_screen(scrn=create_frame()):
       return cv2.putText(scrn, "Face not in range...", (300,768//2 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) 

def no_mask_screen1(scrn=create_frame()):
       return cv2.putText(scrn, "PLEASE WEAR YOUR MASK TO GAIN ENTRY", (150,768//2 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) 

def no_mask_screen2(scrn=create_frame()):
       return cv2.putText(scrn, "Sorry. No access granted since you are not wearing a mask!", (30,768//2 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255), 2, cv2.LINE_AA) 

def temp_screen(scrn=create_frame()):
       scrn=cv2.putText(scrn, "Please place your wrist near the Thermopile Sensor", (60,768//2 -10 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) 
       return cv2.putText(scrn, "to measure your Body Temperature", (180,768//2+20 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) 

def no_temp_screen1(temp,scrn=create_frame()):
       scrn=edit_frame(scrn,True,temp,False,None,None)
       scrn=cv2.putText(scrn, "Temperature beyond permissible limits.", (230,768 -200 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1, cv2.LINE_AA) 
       return cv2.putText(scrn, "Please try again by placing your wrist closer to the Thermopile sensor.", (80,768-150 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1, cv2.LINE_AA) 

def no_temp_screen2(scrn=create_frame()):
       scrn= cv2.putText(scrn, "Sorry. No access granted since your temperature is", (30,768//2-10 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA) 
       return cv2.putText(scrn, " beyond acceptable limits!", (280,768//2 +30), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA) 

def oxy_screen(scrn=create_frame()):
       scrn=cv2.putText(scrn, "Please place your finger in the Pulse Oximeter slot ", (60,768//2 -10 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) 
       return cv2.putText(scrn, "to measure your Body Oxygen Levels", (180,768//2+20 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2, cv2.LINE_AA) 

def no_oxy_screen1(temp,oxy,scrn=create_frame()):
       scrn=edit_frame(scrn,True,temp,True,oxy,False)
       scrn=cv2.putText(scrn, "Oxygen below permissible limits.", (230,768 -200 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1, cv2.LINE_AA) 
       return cv2.putText(scrn, "Please try again by placing your finger on the Pulse Oximeter sensor.", (80,768-150 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 1, cv2.LINE_AA) 

def no_oxy_screen2(scrn=create_frame()):
       scrn= cv2.putText(scrn, "Sorry. No access granted since your Oxygen levels are", (30,768//2-10 ), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA) 
       return cv2.putText(scrn, " below acceptable limits!", (280,768//2 +30), 
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA) 

def edit_frame(frame,mask,tempVal,tempBool,oxyVal,oxyBool):
       
       
       h,w,c=frame.shape
       boxh=h//4
       boxw=w//4

       frame=title(frame)
                               
       #print(str(w)+','+str(h)+','+str(boxw)+','+str(boxh))
              
       frame = cv2.putText(frame, 'MASK', (w-boxw+10,0*boxh+150), cv2.FONT_HERSHEY_COMPLEX,  
                               0.7, (255,255,255), 1, cv2.LINE_AA) 
       
       frame = cv2.putText(frame, 'YES' if mask else 'NO MASK', (w-boxw+16,0*boxh+210), cv2.FONT_HERSHEY_COMPLEX,  
                               1.4, (0,255,0) if mask else (0,0,255), 2, cv2.LINE_AA) 
     
       if tempVal is not None:
              tempVal =round(tempVal,2)
              
              frame = cv2.putText(frame, 'TEMPERATURE', (w-boxw+10,1*boxh+130), cv2.FONT_HERSHEY_COMPLEX,  
                                      0.7, (255,255,255), 1, cv2.LINE_AA) 
              
              frame = cv2.putText(frame, str(tempVal), (w-boxw+16,1*boxh+190), cv2.FONT_HERSHEY_COMPLEX,  
                                      1.4, (0,255,0) if tempBool else (0,0,255), 2, cv2.LINE_AA) 
              
              if oxyVal is not None:
                     
                     oxyVal =round(oxyVal,2)
                     
                     frame = cv2.putText(frame, 'OXYGEN', (w-boxw+10,2*boxh+110), cv2.FONT_HERSHEY_COMPLEX,  
                                             0.7, (255,255,255), 1, cv2.LINE_AA) 
                     
                     frame = cv2.putText(frame, str(oxyVal), (w-boxw+16,2*boxh+170), cv2.FONT_HERSHEY_COMPLEX,  
                                             1.4,  (0,255,0) if oxyBool else (0,0,255), 2, cv2.LINE_AA) 
       
       return frame


right=[np.array([[[100,  19]],

       [[ 99,  20]],

       [[ 91,  27]],

       [[ 79,  39]],

       [[ 76,  44]],

       [[ 73,  47]],

       [[ 69,  54]],

       [[ 66,  57]],

       [[ 65,  60]],

       [[ 63,  62]],

       [[ 62,  65]],
       
       [[ 58,  72]],

       [[ 57,  73]],

       [[ 56,  76]],

       [[ 55,  77]],

       [[ 54,  80]],

       [[ 51,  85]],

       [[ 50,  84]],

       [[ 49,  79]],

       [[ 48,  78]],

       [[ 47,  74]],

       [[ 46,  73]],

       [[ 45,  70]],

       [[ 43,  68]],

       [[ 38,  66]],

       [[ 37,  67]],

       [[ 36,  67]],

       [[ 33,  70]],

       [[ 34,  70]],

       [[ 39,  75]],

       [[ 39,  76]],

       [[ 40,  77]],

       [[ 40,  78]],

       [[ 41,  79]],

       [[ 41,  81]],

       [[ 42,  82]],
       
       [[ 45,  90]],

       [[ 45,  92]],

       [[ 46,  93]],

       [[ 47,  99]],

       [[ 48, 100]],

       [[ 49, 102]],

       [[ 51, 100]],

       [[ 52, 100]],

       [[ 56,  93]],

       [[ 57,  92]],

       [[ 57,  89]],

       [[ 58,  88]],

       [[ 58,  87]],

       [[ 60,  82]],

       [[ 61,  81]],

       [[ 64,  73]],

       [[ 65,  72]],

       [[ 66,  69]],

       [[ 67,  68]],

       [[ 73,  58]],

       [[ 74,  55]],

       [[ 76,  53]],
       
       [[ 80,  46]],

       [[ 82,  43]],

       [[ 85,  40]],

       [[ 89,  35]],

       [[ 89,  34]],

       [[101,  20]]], dtype=np.int32)]
       
wrong=[np.array([[[ 30,   0]],

       [[ 29,   1]],

       [[ 28,   1]],

       [[ 17,  12]],

       [[ 17,  13]],

       [[ 16,  14]],

       [[ 15,  14]],

       [[ 14,  15]],

       [[ 14,  16]],

       [[ 13,  17]],

       [[ 12,  17]],

       [[ 11,  18]],

       [[ 11,  19]],

       [[ 10,  20]],

       [[ 10,  24]],

       [[ 11,  25]],

       [[ 11,  28]],

       [[ 12,  29]],

       [[ 12,  31]],

       [[ 13,  32]],

       [[ 13,  33]],

       [[ 14,  34]],

       [[ 14,  36]],

       [[ 15,  37]],

       [[ 15,  39]],

       [[ 16,  40]],

       [[ 16,  41]],

       [[ 17,  42]],

       [[ 17,  43]],

       [[ 18,  44]],

       [[ 18,  46]],

       [[ 19,  47]],

       [[ 19,  48]],

       [[ 20,  49]],

       [[ 20,  50]],

       [[ 21,  51]],

       [[ 21,  52]],

       [[ 22,  53]],

       [[ 22,  54]],

       [[ 23,  55]],

       [[ 23,  56]],

       [[ 24,  57]],

       [[ 24,  58]],

       [[ 25,  59]],

       [[ 25,  60]],

       [[ 26,  61]],

       [[ 26,  62]],

       [[ 27,  63]],

       [[ 27,  64]],

       [[ 28,  65]],

       [[ 28,  66]],

       [[ 30,  68]],

       [[ 30,  69]],

       [[ 31,  70]],

       [[ 31,  73]],

       [[ 32,  74]],

       [[ 32,  76]],

       [[ 31,  77]],

       [[ 31,  78]],

       [[ 29,  80]],

       [[ 29,  81]],

       [[ 27,  83]],

       [[ 27,  84]],

       [[ 25,  86]],

       [[ 25,  87]],

       [[ 23,  89]],

       [[ 23,  90]],

       [[ 21,  92]],

       [[ 21,  93]],

       [[ 19,  95]],

       [[ 19,  96]],

       [[ 18,  97]],

       [[ 18,  98]],

       [[ 16, 100]],

       [[ 16, 101]],

       [[ 15, 102]],

       [[ 15, 103]],

       [[ 14, 104]],

       [[ 14, 105]],

       [[ 12, 107]],

       [[ 12, 108]],

       [[  9, 111]],

       [[  9, 112]],

       [[  8, 113]],

       [[  8, 114]],

       [[  6, 116]],

       [[  6, 117]],

       [[  4, 119]],

       [[  4, 120]],

       [[  3, 121]],

       [[  3, 122]],

       [[  2, 123]],

       [[  2, 124]],

       [[  1, 125]],

       [[  1, 126]],

       [[  0, 127]],

       [[  4, 127]],

       [[  5, 126]],

       [[  7, 126]],

       [[  8, 125]],

       [[  9, 125]],

       [[ 10, 124]],

       [[ 11, 124]],

       [[ 12, 123]],

       [[ 13, 123]],

       [[ 15, 121]],

       [[ 16, 121]],

       [[ 19, 118]],

       [[ 20, 118]],

       [[ 25, 113]],

       [[ 26, 113]],

       [[ 30, 109]],

       [[ 31, 109]],

       [[ 44,  96]],

       [[ 44,  95]],

       [[ 48,  91]],

       [[ 49,  91]],

       [[ 50,  92]],

       [[ 52,  92]],

       [[ 53,  93]],

       [[ 54,  93]],

       [[ 57,  96]],

       [[ 58,  96]],

       [[ 60,  98]],

       [[ 61,  98]],

       [[ 62,  99]],

       [[ 63,  99]],

       [[ 65, 101]],

       [[ 67, 101]],

       [[ 68, 102]],

       [[ 69, 102]],

       [[ 70, 103]],

       [[ 72, 103]],

       [[ 73, 104]],

       [[ 75, 104]],

       [[ 76, 105]],

       [[ 78, 105]],

       [[ 79, 106]],

       [[ 81, 106]],

       [[ 82, 107]],

       [[ 86, 107]],

       [[ 87, 108]],

       [[ 90, 108]],

       [[ 91, 109]],

       [[ 98, 109]],

       [[ 99, 110]],

       [[104, 110]],

       [[105, 109]],

       [[108, 109]],

       [[109, 108]],

       [[110, 108]],

       [[111, 107]],

       [[113, 107]],

       [[115, 105]],

       [[116, 105]],

       [[117, 104]],

       [[118, 104]],

       [[120, 102]],

       [[121, 102]],

       [[122, 101]],

       [[123, 101]],

       [[125,  99]],

       [[126,  99]],

       [[127,  98]],

       [[125,  98]],

       [[124,  97]],

       [[121,  97]],

       [[120,  96]],

       [[119,  96]],

       [[118,  95]],

       [[115,  95]],

       [[114,  94]],

       [[111,  94]],

       [[110,  93]],

       [[108,  93]],

       [[107,  92]],

       [[104,  92]],

       [[103,  91]],

       [[102,  91]],

       [[101,  90]],

       [[ 99,  90]],

       [[ 98,  89]],

       [[ 96,  89]],

       [[ 95,  88]],

       [[ 93,  88]],

       [[ 92,  87]],

       [[ 91,  87]],

       [[ 90,  86]],

       [[ 88,  86]],

       [[ 86,  84]],

       [[ 85,  84]],

       [[ 84,  83]],

       [[ 83,  83]],

       [[ 82,  82]],

       [[ 81,  82]],

       [[ 80,  81]],

       [[ 79,  81]],

       [[ 77,  79]],

       [[ 76,  79]],

       [[ 67,  70]],

       [[ 67,  68]],

       [[ 68,  67]],

       [[ 68,  65]],

       [[ 70,  63]],

       [[ 70,  62]],

       [[ 72,  60]],

       [[ 72,  59]],

       [[ 75,  56]],

       [[ 75,  55]],

       [[ 78,  52]],

       [[ 78,  51]],

       [[ 81,  48]],

       [[ 81,  47]],

       [[ 83,  45]],

       [[ 83,  44]],

       [[ 86,  41]],

       [[ 86,  40]],

       [[ 88,  38]],

       [[ 88,  37]],

       [[ 90,  35]],

       [[ 90,  33]],

       [[ 91,  32]],

       [[ 91,  30]],

       [[ 92,  29]],

       [[ 92,  27]],

       [[ 93,  26]],

       [[ 93,  25]],

       [[ 92,  24]],

       [[ 89,  24]],

       [[ 88,  23]],

       [[ 83,  23]],

       [[ 82,  22]],

       [[ 76,  22]],

       [[ 75,  21]],

       [[ 72,  21]],

       [[ 71,  22]],

       [[ 67,  22]],

       [[ 65,  24]],

       [[ 65,  25]],

       [[ 63,  27]],

       [[ 63,  28]],

       [[ 60,  31]],

       [[ 60,  32]],

       [[ 58,  34]],

       [[ 58,  35]],

       [[ 56,  37]],

       [[ 56,  38]],

       [[ 54,  40]],

       [[ 54,  41]],

       [[ 52,  43]],

       [[ 52,  44]],

       [[ 50,  46]],

       [[ 49,  46]],

       [[ 48,  45]],

       [[ 48,  44]],

       [[ 46,  42]],

       [[ 46,  41]],

       [[ 45,  40]],

       [[ 45,  39]],

       [[ 43,  37]],

       [[ 43,  36]],

       [[ 42,  35]],

       [[ 42,  33]],

       [[ 41,  32]],

       [[ 41,  31]],

       [[ 40,  30]],

       [[ 40,  29]],

       [[ 39,  28]],

       [[ 39,  26]],

       [[ 38,  25]],

       [[ 38,  23]],

       [[ 37,  22]],

       [[ 37,  21]],

       [[ 36,  20]],

       [[ 36,  17]],

       [[ 35,  16]],

       [[ 35,  13]],

       [[ 34,  12]],

       [[ 34,  10]],

       [[ 33,   9]],

       [[ 33,   6]],

       [[ 32,   5]],

       [[ 32,   2]],

       [[ 31,   1]],

       [[ 31,   0]]], dtype=np.int32)]



