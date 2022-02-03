import cv2 as cv
import numpy as np
import sys
import matplotlib
import colordetect

#general idea:
# 1. use colordetect to detect 4 tape fingers
# 2. use opencv hand gesture detection for L-frame shapes
# 3. use gesture to trigger the screen cap 
# 4. crop photo to fit into dimensions of hand frame
# 5. export photo to output display