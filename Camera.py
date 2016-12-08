import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
#cap.set(3, 640)
#cap.set(4, 480)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
''' Using the mouse to draw on the image '''
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(frame,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(frame,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(frame,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(frame,(x,y),5,(0,0,255),-1)

while(cap.isOpened()):
    e1 = cv2.getTickCount() # get the start execution time

    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret==True:
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #frame = cv2.flip(frame,0)
        # write the flipped frame
        #out.write(frame)
        
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        #Draw shapes onto the image
        # Draw a diagonal blue line with thickness of 5 px
        #frame = cv2.line(frame,(0,0),(511,511),(255,0,0),5)
        #frame = cv2.rectangle(frame,(384,0),(510,128),(0,255,0),3)
        #frame = cv2.circle(frame,(447,63), 63, (0,0,255), 10)
        
        # arguments (center location (x,y), (major axis length, minor axis length), 
        # angle in anti-clockwise, start angle, end angle, BGR colour, line thickness Fill=-1)
        #frame = cv2.ellipse(frame,(256,256),(100,50),23,63,235,(95,122,122),-1)
        
        # polygon
        #pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
        #pts = pts.reshape((-1,1,2))
        #frame = cv2.polylines(frame,[pts],True,(0,255,255))
        
        # text
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(frame,'OpenCV',(10,450), font, 4,(255,255,255),2,cv2.LINE_AA)
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        #cv2.setMouseCallback('image',draw_circle)
        
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        ''' pixel manipulation '''
        #px = frame.item(10,10,2)
        #print "pixel [100, 100] colour value = ", px

        # accessing only blue pixel
        #blue = frame[100,100,0]
        #print 'blue ',blue
        
        # modifying RED value
        #frame.itemset((10,10,2),100)
        #frame.item(10,10,2)
        
        # copy a section of the image to another loacation
        #ball = frame[280:340, 330:390]
        #frame[273:333, 100:160] = ball
        
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # define range of blue color in HSV
        #lower_blue = np.array([110,50,50])
        #upper_blue = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        #mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(frame,frame, mask= mask)

        #cv2.imshow('frame',frame)
        #cv2.imshow('mask',mask)
        #cv2.imshow('res',res)
        
        #green = np.uint8([[[0,255,0 ]]])
        #hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
        
        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

        
        
        # split the image to BGR
        #b,g,r = cv2.split(frame)
        # buld an image with three arrays b,g,r
        #frame = cv2.merge((b,g,r))

        # Display the resulting frame
        #cv2.imshow('frame',hsv_green)
        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
    e2 = cv2.getTickCount() # get the end exectution time
    time = (e2 - e1)/ cv2.getTickFrequency() # execution time
    print "Execution time was ", time, 's'

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()