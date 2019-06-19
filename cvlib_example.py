"""Example using cvlib."""
"""Documentation: https://github.com/arunponnusamy/cvlib"""
try:
    import cvlib as cv
except:
    exit("must pip3 install cvlib first")
from cvlib.object_detection import draw_bbox
import cv2

img = image = cv2.imread("assets/sv.jpg")
bbox, label, conf = cv.detect_common_objects(img, model="largess")
print(label)

output_image = draw_bbox(img, bbox, label, conf)
cv2.imwrite("cvlib-example-out.jpg", output_image)
