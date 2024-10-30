import time  #for checking frae rate
import mediapipe as mp
import cv2

cap=cv2.VideoCapture(0) # to capture videos 

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw=mp.solutions.drawing_utils #mediapipe methode to draw line b/w two points 
pTime = 0 #for privious time 
cTime = 0 #for current time 
#both are for FPS

while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB) 
#processing but not showing anythingh because we are not printing anything so we are using print in next line 
    print(results.multi_hand_landmarks)    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if id==0:
#Draw a circle at a particular id (id=0)
#And if we remove this if then it will draw for every point but there is no need because we had already drawan for each point 
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)
#HAND_CONNECTIONS is for joining points through lines 

    cTime = time.time() #It will give us FPS
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
#Above line will display fps in integer format
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
    
'''Through this we can track all points in a list and use it for furthur use 
and now we can convert this program in a module so if we need this in future 
project ,we can easily use it without writing again.'''    
    
    