from rembg import remove
import cv2

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
cv2.imwrite(r"Images\demo.jpg", removeBgImg)

remImg = cv2.imread(r"Images\demo.jpg")

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
    cv2.imwrite(r"Images\demo.png", remImg)
    if cv2.waitKey(1) & 0xFF == 113:  # press "q" to exit
        break

cv2.destroyAllWindows()