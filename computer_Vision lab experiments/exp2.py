import cv2
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    blur = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur Image", blur)
    cv2.imwrite("blur_output.png", blur)
    print("Blurred image saved as blur_output.png")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
