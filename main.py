import cv2

src = cv2.imread('cat.jpg',cv2.IMREAD_UNCHANGED)
#cv2.imshow("This is a cat",src)
cv2.waitKey(0)

resize_percent = 50

new_width = int(src.shape[1]*resize_percent/100)
new_height = int(src.shape[0]*resize_percent/100)

output = cv2.resize(src,(new_width,new_height))

cv2.imwrite('final.jpg',output)