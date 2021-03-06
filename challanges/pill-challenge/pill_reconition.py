import cv2
import numpy as np
def imgproc(frame):
    
    # convert color to gray scale and show it
    
    background = np.full_like(frame, 0)
    background[:,:,1] = 162
    background[:,:,2] = 14
    
    
    img = frame - background
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # convert image to black and white and show it
    thresh1, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    
    # find contours!
    contours, hry = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # draw all the contours
    cpframe = frame.copy()
    cv2.drawContours(cpframe, contours, -1, (255,0,0), 3)
    cv2.imshow('contours', cpframe)
    
    # ================== TODO ===================
    
    # Every pill is surrounded by a contour in variable "contours" now
    
    # ============================================
    
    for ctr in contours:
        m = cv2.mean(ctr)
        org = int(m[0]), int(m[1])
        cv2.putText(frame, "pill", org, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    return frame

if __name__ == "__main__":
    pills = cv2.imread('pill.png')
    cv2.imshow('pill challenge',imgproc(pills))
    cv2.waitKey(0)