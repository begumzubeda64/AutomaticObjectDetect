from rembg import remove     # https://github.com/danielgatis/rembg
import cv2       # pip install opencv-python
import cvzone    # pip install cvzone

# Read Image
# Images\1.jpg
imgPath = input(r"Enter image path: ")
srcImg = cv2.imread(imgPath)

# Resize Image
width = 1200
height = 700
points = (width, height)
resizedImg = cv2.resize(srcImg, points, interpolation=cv2.INTER_LINEAR)

# Select ROI
# "Select a ROI and then press SPACE or ENTER button!"
# "Cancel the selection process by pressing c button!"
r = cv2.selectROI("Select the area", resizedImg)
(xi, yi, w, h) = r

# Crop image
croppedImg = resizedImg[yi: yi + h, xi: xi + w]
cv2.imshow("Cropped", croppedImg)

# Remove Background
removeBgImg = remove(croppedImg)
cv2.imwrite(r"Images\remove.png", removeBgImg)

remImg = cv2.imread(r"Images\remove.png")

run = False
def draw_outline(event, x, y, flags, param):
    global run
    if event == cv2.EVENT_LBUTTONDOWN:
        run = True
        cv2.circle(remImg, (x, y), 3, (0, 255, 0), 1)

    if event == cv2.EVENT_LBUTTONUP:
        run = False

    if event == cv2.EVENT_MOUSEMOVE:
        if run == True:
            cv2.circle(remImg, (x, y), 3, (0, 0, 255), 1)

cv2.namedWindow(winname="Removed Background")
cv2.setMouseCallback("Removed Background", draw_outline)

while True:
    # Display Image
    cv2.imshow("Removed Background", remImg)

    if cv2.waitKey(1) & 0xFF == 113:  # press "q" to exit
        cv2.imwrite(r"Images\outline.png", remove(remImg))
        cv2.destroyWindow("Cropped")
        cv2.destroyWindow("Select the area")
        cv2.destroyWindow("Removed Background")
        break

# Overlay
finalImg = cv2.imread(r"Images\outline.png", cv2.IMREAD_UNCHANGED)
imgResult = cvzone.overlayPNG(resizedImg, finalImg, [xi, yi])

while True:
    cv2.imshow("Output", imgResult)
    if cv2.waitKey(0) & 0xFF == 113:  # press "q" to exit
        cv2.destroyWindow("Output")
        break


