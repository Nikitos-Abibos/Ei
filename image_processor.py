import cv2
import numpy as np

def create_contour_image(image_path, width=None, height=None):
    image = cv2.imread(image_path)
    
    if width is not None and height is not None:
        resized_image = cv2.resize(image, (width, height))
    else:
        resized_image = image 

    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 1.5)
    edges = cv2.Canny(blurred, 50, 100)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(edges, -1, kernel)

    contour_image = cv2.cvtColor(sharpened, cv2.COLOR_GRAY2RGB)
    return contour_image
