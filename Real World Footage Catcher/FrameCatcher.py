# Imports
import cv2
import time

# Counter
i = 0

# Timepoint
settime = 24000 # Adjusts start time for video

vidcap = cv2.VideoCapture('D:\Rivers\Test 4 - Craignahorna\Test 3\MVI_5439.MOV')
vidcap.set(cv2.CAP_PROP_POS_MSEC,settime)    # Sets Video start time
while (vidcap.isOpened()):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,settime) # Set video strat time plus incrementor

    # Read the Video
    success,image = vidcap.read() 

    # Save the file
    cv2.imwrite("D://New Images//Exp 4//Evening//"+'EveningBagExp4_'+str(i)+'.jpg', image)

    # Add to counter
    i+=1

    # Increase time point in footage
    settime+=250 # Fast forward video, (+1000 for slower moving streams)

    # Take no more than 10 frames
    if i%11 == 0:
        break

# Close the video playback
cv2.destroyAllWindows()


