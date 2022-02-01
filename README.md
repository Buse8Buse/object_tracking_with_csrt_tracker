# object_tracking_with_csrt_tracker
Object tracking was performed with the CSRT Tracker algorithm.

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

## CSRT ile ayırt edici korelasyon filtrelerinin ana adımları boyunca ayrıştırılan tek bir yineleme işleme süresi 
![image](https://user-images.githubusercontent.com/81264301/152055086-63609eac-6b5b-4501-aaa3-c19b6faf7004.png)

## Note

-When the final version of the code is run, the desired follow-up in the video
When we draw a frame around the object and then press 'ENTER', it will appear with the frame around it.
If even a small point is clear when he starts to move together and encounters some obstacles
tracking continues, but if the frame is too small and the tracked object is invisible.
If it is completely lost, the tracking ends and the object disappears.

-So your bounding box is a little bit
Choosing a large size will facilitate the tracking of the object. When I set small frame
I observed frequent deviations from the target.


