# object_tracking_with_csrt_tracker

Object tracking was performed with the CSRT Tracker algorithm.

# What is Object Tracking ?

-Simply,
Finding an object in consecutive frames of a video is called object tracking.

Face detector in a video operating and the person's face is obscured by an object, the face detector is likely will fail.

On the other hand, a good tracking algorithm can handle a certain level of congestion.
will.

An image or video, single or multi, in many areas of daily life.
applied on. Security-entertainment-daily life-crime detection etc. like many more
can be used for any reason.

## What is CSRT Tracker?

Channel and Spatial Reliability with Discriminant Correlation Filter (DCF-CSR), for monitoring
spatial reliability map to adjust the filter support to the part of the selected region from the frame.
we are using. This allows enlargement and localization of the selected region and non-rectangular
provides better tracking of regions or objects. Uses only 2 standard features (HoGs and
Color Names). It also runs at a relatively lower fps (25 fps), but is more for object tracking.
provides high accuracy.

## Requirement & Installation

The functions of OpenCV, which is a very useful library for image processing, are used to carry out the steps of the project.

To install the script you only need to download the Repository. To Run the script you have to had installed:

-OpenCV

-Python

## A single iteration processing time parsed through the main steps of CSRT and discriminant correlation filters
![image](https://user-images.githubusercontent.com/81264301/152055086-63609eac-6b5b-4501-aaa3-c19b6faf7004.png)


Tracker adjustments, edits of information about the bounding box, image FPS information and information on the size and positions to be displayed and on the image
size- location information- font- shape- number of images to be displayed per second, etc.
The settings are as shown in the code fragments below and are included in the code.

## Note

-When the final version of the code is run, the desired follow-up in the video
When we draw a frame around the object and then press 'ENTER', it will appear with the frame around it.
If even a small point is clear when he starts to move together and encounters some obstacles
tracking continues, but if the frame is too small and the tracked object is invisible.
If it is completely lost, the tracking ends and the object disappears.

-So your bounding box is a little bit
Choosing a large size will facilitate the tracking of the object. When I set small frame
I observed frequent deviations from the target.

![image](https://user-images.githubusercontent.com/81264301/152068981-dbb41f53-2cfe-461e-bbc5-c54956977b9f.png)

![image](https://user-images.githubusercontent.com/81264301/152069016-592fab83-2828-425a-bc9a-e7fb2c13284b.png)

![image](https://user-images.githubusercontent.com/81264301/152069039-619d1573-d8f6-4a7c-92c5-c75a097c520e.png)

![image](https://user-images.githubusercontent.com/81264301/152128910-215c0d0d-a116-4bc9-8629-035083c84dfc.png)

![image](https://user-images.githubusercontent.com/81264301/152129001-4f70086b-10c5-4c31-9c19-8be96ef4985a.png)

## Finally

In my work, I used a video that includes a single vehicle on the road.

You can also use a video or webcam with the object you want to track.

Simply write the 'path' of the data you will use in the piece of code specified as im = cv2.VideoCapture('Test_2.mp4') .

Or if you want to work on the webcam
Just write im = cv2.VideoCapture(0)

