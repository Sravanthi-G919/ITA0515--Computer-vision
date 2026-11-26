import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    cv2.imshow("Original Grayscale Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)
    cv2.imwrite("equalized_output.png", equalized)
    print("Equalized image saved as equalized_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
