#!/usr/bin/python3
import  cv2
import numpy as np
import random
face_cascade = cv2.CascadeClassifier('a.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')   #eye detection


cap=cv2.VideoCapture(0)
while True:
	status,img=cap.read()
	grayimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grayimg,1.15,5)  
	#image_faces=[]    // other way to store face images
	for  (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
		roi_gray=grayimg[y:y+h,x:x+w]
		#image_faces.append(grayimg[y:y+h,x:x+w])  // other way to store face images
		#for i,facee in enumerate(image_faces) :   // other way to store face images
		x=random.random()          #storing detected images
		y=str(x)[2:6]
		cv2.imwrite('mudit' +y+'.jpg',roi_gray)

		eyes = eye_cascade.detectMultiScale(roi_gray)    #eye_detection_process
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
			roi_gray=img[y:y+h,x:x+w]
			
			
	cv2.imshow('imgw',img)
	if cv2.waitKey(30) & 0xff == ord('q'):
		break		
cap.release()
cv2.destroyAllWindows()
