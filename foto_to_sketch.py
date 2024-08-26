import cv2
image_path = input("naam foto")
image = cv2.imread(image_path)
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(grey_img, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invert, scale=256.0)

cv2.imwrite("sketch.png", sketch)