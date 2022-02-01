import numpy
import matplotlib
import cv2 as cv
import sys

#print( cv.__version__)
path = r"hammie.jpg"
print(path)
img = cv.imread(path)
dimensions = img.shape
h = dimensions[0]
w = dimensions[1]
img2 = cv.resize(img, dsize=(w//5,h//5), interpolation=cv.INTER_AREA) #how to access dimensions of image
# note abt interpolation: use CUBIC/LINEAR for enlarging, use AREA for shrinking
if img is None:
    sys.exit("could not load image")
#cv.imshow("window", img2)

#convert to grayscale
gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray", gray)

#BGR to HSV
hsv = cv.cvtColor(img2, cv.COLOR_BGR2HSV)
#cv.imshow("HSV", hsv)

#BGR to L*a*b
lab = cv.cvtColor(img2, cv.COLOR_BGR2LAB)
#cv.imshow("LAB", lab)

#blur
blur = cv.GaussianBlur(img2, (3, 3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#edge cascade
edge = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Edges', edge)

#threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)
#looks at an image and tries to binarize it; this or canny are ways to contourize an image

#contour detection
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# looks at structure of image/edges found (canny argument)
# hierarchical rep of contours (e.g. square within rectangle, circle within square, etc)
#RETR_LIST - mode in which findContours finds contours, List returns all contours
#CHAIN_APPROX_NONE - contour approximation method. This one does nothing, just returns all contours
#CHAIN_APPROX_SIMPLE - compresses
print(f'{len(contours)} contour(s) found')

#draw contours of image on a blank image
blank = numpy.zeros(img2.shape[:2], dtype = "uint8")
#cv.imshow('Blank', blank)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
#image, contours, contour index, color, thickness
#cv.imshow('Contours Drawn', blank)

#color channels - split an image into its respective color channels
b, g, r = cv.split(img2)

print(img2.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("merged", merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
#cv.imshow("B", blue)
#cv.imshow("G", green)
#cv.imshow("R", red)

#dilating image, brightens edge detected image
dil = cv.dilate(edge, (3,3), iterations=1) # increased iterations means increased thickness
#cv.imshow('dilated', dil)

#cropping
crop = img2[50:200, 200:400]
#cv.imshow('cropped', crop)

def translate(img, x, y):
    trans = numpy.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans, dim)

translated = translate(img2, 100, 100) # shifts 100 right, 100 down
#cv.imshow("window", translated)

def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (w//2, h//2)
    rot = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dim = (w, h)
    return cv.warpAffine(img, rot, dim)

rotated = rotate(img2, 30) # rotates 30 deg CCW
#cv.imshow("window", rotated)

key = cv.waitKey(0)
#cv2.destroyAllWindows()
if key == ord("s"):
    cv.imwrite("hammie2.png", img)