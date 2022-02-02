# extract and save video frames.

import cv2
im = cv2.VideoCapture('Test_2.mp4')

# Now create a CSRT Tracker.
tracker = cv2.TrackerCSRT_create()

# Run the code below to display the image on the screen.
success, photo = im.read()

# BBOX parameter refers to the frame in which the output data is contained.(Bounding box)

# selectROI() function automatically shows us the image and allows us to manually select the ROI in the image.

# !!!!!!!!!!!!!!! After selecting the ROI we need to press or enter the space button to advance to the selected area !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#In creating a single bounding box it was important that the last parameter of cv2.selectROI was 'False'.
bbox = cv2.selectROI("Tracking.",photo,False)
tracker.init(photo,bbox)

# A rectangular box is determined and the data falling into this box is requested from the server.

# Frame boundaries are determined as minX, minyY maxX, MaxY.
def drawBox(photo,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(photo,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(photo, "Tracking.", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),3)

while True:
    # 'cv2.getTickCount()' is the number of clock cycles after a reference event (such as when the machine is turned on) until this function is called.

    # 'cv2.get Tick Frequency()' returns the frequency of clock cycles or the number of clock cycles per second.

    # The timer has been set here.
    timer = cv2.getTickCount()

    # Here, settings are made for tracker detection.
    success, photo = im.read()

    success,bbox = tracker.update(photo)
    #print(type(bbox))
    print(bbox)

    if success:
        drawBox(photo,bbox)
    else:
        cv2.putText(photo,"Object Disappeared.",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    # Necessary settings are being made to calculate the number of images per second.
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    # 'putText' overwrites the image.

    # The text to be printed as a parameter to this function, the coordinate where the text will start, the font information, color and thickness values are below.

    # Here image size-font-RGB space etc. adjustments and in the last parameter, font thickness adjustment is made.
    cv2.putText(photo,str(int(fps)),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    # Here, when the video is cut, the framed image is followed when the video is played and displayed with the text "Tracker".
    cv2.imshow("Tracker",photo)

    # 'cv2.waitKey(1)' returns the character code of the currently pressed key and '-1' if no key is pressed.

    # When returning a non-single-byte code, 'n & 0xFF' is a binary 'AND operation' to ensure that only the single-byte (ASCII) representation of the key remains.

    # Always returns the ASCII representation of 'q' which is 113 (0x71 in hexadecimal)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
