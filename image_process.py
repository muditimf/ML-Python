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

"""
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
        print("Give coordinates in 20,20 format")
        st_pt=[(input("enter starting coordinates"))]
        ed_pt=[(input("enter ending coordinates"))]
        color=[(input("enter colour combination"))]
        line_width=[(input("enter line width"))]
        cv2.line(img,st_pt,ed_pt,color,line_width)
        cv2.imshow("Line",img)
        cv2.waitKey(0)
"""
#line
cv2.line(img,(0,0),(50,50),(255,167,24),2)

#rectangle
cv2.rectangle(img,(20,20),(150,150),(0,234,1),3)

#circle
cv2.circle(img,(100,100),20,(23,0,0),1)


#text
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Dog style',(0,130),font,1,(255,45,0),2,cv2.LINE_AA)
cv2.imshow("dogg",img)


cv2.waitKey(0)
