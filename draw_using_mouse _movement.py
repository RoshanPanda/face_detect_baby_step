import cv2
import numpy as np

#variables
drawing = False
ix,iy = -1,-1


#function

def draw_rect(event, x, y, flags, params):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)

#image show


img=np.zeros((512,512,3))

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw_rect)
while True:
    cv2.imshow("window", img)
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
