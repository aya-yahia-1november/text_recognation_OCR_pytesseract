import  cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"D:\apps_dowonload\Tesseract-OCR\tesseract.exe"
image =cv2.imread("text.jpeg")
gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
config="--psm 3 "
text =pytesseract.image_to_string(adaptive,config=config,lang="eng")
print(text)
cv2.imshow("gray",gray)
cv2.imshow("adaptiv",adaptive)
cv2.waitKey(0)
cv2.destroyWindow()