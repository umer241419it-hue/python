import cv2

scale_percent = 50
source = r"C:\Users\kadiw\OneDrive\Desktop\Python\ImageResizer\car.jpeg"
destination = r"C:\Users\kadiw\OneDrive\Desktop\Python\ImageResizer\newImage.jpeg"

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("BMW car", src)

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)

cv2.waitKey(0)
