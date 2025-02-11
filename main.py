import cv2 as cv
import numpy as np



output_path = "output.jpg"

image = cv.imread('photos/photo_1.jpg')

def re_size(frame, scale=0.3):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)                                 # görüntüler büyük geliyordu
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized = re_size(image)

red1 = np.array([0, 120, 70])
red2 = np.array([10, 255, 255])                                       # bu aralıkları internetten buldum
red3 = np.array([170, 120, 70])
red4 = np.array([180, 255, 255])

hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)                          #bgr hsvye çevirdim sadece ana renlkleri görmek için


mask1 = cv.inRange(hsv, red1,red2)
mask2 = cv.inRange(hsv, red3, red4)
mask = mask1 + mask2


contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

if contours:

    largest_contour = max(contours, key=cv.contourArea)
    x, y, g, h = cv.boundingRect(largest_contour)
    cv.rectangle(resized, (x, y), (x + g, y + h), (0, 255, 0), 2)                          # merkez bulmayı biraz araştırıp bulduğum örneklerle
                                                                                           #uyarlamaya çalıştım
    center = (x + g // 2, y + h // 2)
    print("stop merkezi :" + str(center))

cv.imwrite(output_path, resized)

cv.imshow("stop", resized)
cv.waitKey(0)
