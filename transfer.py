import cv2 
import time 
import socket

vid = cv2.VideoCapture('bad_apple.mp4')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345               
s.bind((host, port)) 

success , image = vid.read()
count = 0
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]

while success:
  success,img = vid.read()
  rows,cols,_ = img.shape
  
  img  = cv2.resize(img, (72 , 54), interpolation = cv2.INTER_AREA)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to greyscale
  rows,cols,_ = img.shape # get width and length of img
  
  msg = []
  for i in range(rows):
    new = []
    for j in range(cols):
        k = gray[i,j]
        new.append(ASCII_CHARS[int(k/24)])
    msg.append(new)
  
  #print(msg)
  for i in range(rows):
    op = ""
    for j in range(cols):
        op += msg[i][j]
    print(op)
        #print(msg[i][j])
    #print("\n")
  count += 1
 
  # print(count)
