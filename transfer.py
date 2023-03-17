import cv2 
import time 
import socket
import os
from datetime import datetime , timedelta
import sys 
import subprocess
import playsound
from moviepy.editor import *

vid = cv2.VideoCapture('bad_apple.mp4')
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

success , image = vid.read()
count = 0
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
opt = []

video = VideoFileClip("bad_apple.mp4")
if(not os.path.exists("bad_apple.mp3") ): video.audio.write_audiofile("bad_apple.mp3")

try:
  while success:
    print("Time rendered: " , int(count/fps) , 's')
    print(count/length*100 , "%")
    os.system('cls')

    success,img = vid.read()
    
    # 134 51 -> 121 46
    img  = cv2.resize(img, (134, 51), interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to greyscale
    rows,cols,_ = img.shape # get width and length of img
    
    

    msg = ""
    for i in range(rows):
      for j in range(cols):
          k = gray[i,j] // 24
          msg += ASCII_CHARS[k]
      msg += "\n";
    
    opt.append(msg)
    #os.system('cls')
    #subprocess.call("cls" , shell=True)

    count +=1


except:
  base = datetime.now()
  playsound.playsound("bad_apple.mp3", False)
  count = 0

  for msg in opt:
    count += 1
    subprocess.call("cls" , shell=True)
    sys.stdout.write(msg)
    
    while(base+timedelta(seconds=count/fps) > datetime.now()):
      continue

