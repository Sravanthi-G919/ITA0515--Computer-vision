import cv2
import matplotlib.pyplot as plt
img = cv2.imread("exp1.png")
if img is None:
    print("Error: Image not found!")
else:
    cv2.imshow("Original Image", img)
    colors = ('b', 'g', 'r')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
