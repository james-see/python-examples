"""Example using cvlib."""
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

img = image = cv2.imread("assets/sv.jpg")
bbox, label, conf = cv.detect_common_objects(img, model="largess")
print(label)

output_image = draw_bbox(img, bbox, label, conf)
cv2.imwrite("cvlib-example-out.jpg", output_image)
