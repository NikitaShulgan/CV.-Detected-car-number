import cv2
import pytesseract
from pytesseract import image_to_string
import matplotlib.pyplot as plt
from imutils import contours
image = cv2.imread("example.jpg")

#cv2.imshow("Test", image)

image = cv2.imread("example.jpg", 0)
#cv2.imshow("Test1", image)

height, width = image.shape
BGR2RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#cv2.imshow("Test2", BGR2RGB)

plt.imshow(image,'gray')
#plt.show()

# Adaptive Threshold Mean C
img_thresh_mean_c = cv2.adaptiveThreshold(image, 255,
                                         cv2.ADAPTIVE_THRESH_MEAN_C,
                                         cv2.THRESH_BINARY_INV,
                                         17,-2)
# plot the result
plt.imshow(img_thresh_mean_c, 'gray')
plt.show()

cntrs = cv2.findContours(img_thresh_mean_c, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cntrs, _ = contours.sort_contours(cntrs[0])

pytesseract.pytesseract.tesseract_cmd = r'C:\All files\Programming\TesseractOCR\tesseract.exe'

for c in cntrs:
  area = cv2.contourArea(c)
  x, y, w, h = cv2.boundingRect(c)
  if area > 2000:
    img = image[y:y+h, x:x+w]
    result = pytesseract.image_to_string(img, lang="rus+eng")
    if len(result) > 5:
      print(result)


cv2.waitKey()