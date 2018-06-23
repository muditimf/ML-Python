#!/usr/bin/python3

import cv2

#reading image data
img=cv2.imread("dog.jpeg",1)

#printing dimensions of image
print(img.shape)

#display of image
#cv2.imshow("dogg",img)

#save image 
#cv2.imwrite("dogg.jpeg",img)


#to perform Draw functions

#operations menu


print("Give coordinates in x,y format")
st_xpt=int((input("enter starting x coordinates")))
st_ypt=int((input("enter starting y coordinates")))

ed_xpt=int((input("enter ending x coordinates")))
ed_ypt=int((input("enter ending y coordinates")))

col_1pt=int((input("enter color nos")))
col_2pt=int((input("enter color nos")))
col_3pt=int((input("enter color nos")))

line_width=int((input("enter line width")))

while True:
    print("""
    Press 1: Draw Line
    Press 2: Draw rectangele
    Press 3: Draw circle
    Press 4: Write Text
    """)
    
#taking choice from user
    
    ch=(input("what are u thinking"))
    if int(ch) == 1:
        #line
        cv2.line(img,(st_xpt,st_ypt),(ed_xpt,ed_ypt),(col_1pt,col_2pt,col_3pt),line_width)
        cv2.imshow("Line",img)
        cv2.waitKey(0)

    if int(ch) == 2:
        #rectangle
        cv2.rectangle(img,(st_xpt,st_ypt),(ed_xpt,ed_ypt),(col_1pt,col_2pt,col_3pt),line_width)
        cv2.imshow("rectangle",img)
        cv2.waitKey(0)

    if int(ch) == 3:
        #circle
        c_xpt=int((input("enter starting x center coordinates")))
        c_ypt=int((input("enter starting y center coordinates")))
        radius=int((input("enter radius ")))
        cv2.circle(img,(c_xpt,c_ypt),(radius),(col_1pt,col_2pt,col_3pt),line_width)
        cv2.imshow("circle",img)
        cv2.waitKey(0)

    if int(ch) == 4:
        #text
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=(input("enter text"))
        cv2.putText(img,text,(0,130),font,1,(255,45,0),2,cv2.LINE_AA)
        cv2.imshow("dogg",img)
        cv2.waitKey(0)

