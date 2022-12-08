import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from playsound import playsound


left_hard_vertices = np.array([[130, 210], [70, 150], [80, 100], [100, 90], [65, 95], [40, 155], [60, 220], [120, 215], [130, 210]])
left_mid_vertices = np.array([[135, 205], [125, 125], [130, 90], [155, 80], [100, 90], [80, 100], [70, 150], [130, 210], [135, 205]])
left_bit_vertices = np.array([[155, 80], [145, 90], [140, 200], [135, 205], [125, 125], [130, 90], [155, 80]])
forward_vertices = np.array([[155, 80], [145, 90], [140, 200], [170, 200], [165, 90], [155, 80]])
right_hard_vertices = np.array([[310-130, 210], [310-70, 150], [310-80, 100], [310-100, 90], [310-65, 95], [310-40, 155], [310-60, 220], [310-120, 215], [310-130, 210]])
right_mid_vertices = np.array([[310-135, 205], [310-125, 125], [310-130, 90], [310-155, 80], [310-100, 90], [310-80, 100], [310-70, 150], [310-130, 210], [310-135, 205]])
right_bit_vertices = np.array([[155, 80], [310-145, 90], [310-140, 200], [310-135, 205], [310-125, 125], [310-130, 90], [310-155, 80]])
backward_vertices = np.array([[135, 220], [310-135, 220], [310-120, 240], [120, 240], [135, 220]])
u_left_vertices = np.array([[125, 225], [115, 220], [65, 225], [90, 250], [110, 245], [125, 225]])
u_right_vertices = np.array([[310-125, 225], [310-115, 220], [310-65, 225], [310-90, 250], [310-110, 245], [310-125, 225]])


img = cv.imread("test.png")
liste = [forward_vertices, left_bit_vertices, left_mid_vertices, left_hard_vertices, right_bit_vertices, right_hard_vertices, right_mid_vertices, backward_vertices, u_left_vertices, u_right_vertices]

for x in liste:
    y = -1
    z = -1
    for i, j in x:

        if y != -1 and z != -1:
            cv.line(img, (y, z), (i, j), (0, 0, 255), 2)

        y = i
        z = j


img_2 = cv.imread("test.png")
blue_lower = np.array([180, 160, 0])
blue_upper = np.array([255, 255, 150])
u_right_mask = cv.inRange(img_2, blue_lower, blue_upper)
# conts, _ = cv.findContours(u_right_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# cv.drawContours(img, conts, -1, (255, 0, 0), 2)

while True:
    cv.imshow("image", img)
    cv.imshow("image_2", img_2)
    cv.imshow("mask", u_right_mask)
    if cv.waitKey(10) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()

playsound("ses_deneme.mp3")