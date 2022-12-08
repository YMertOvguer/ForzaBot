# importing libs
import pyautogui as pyaut
from screeninfo import get_monitors as getm
import numpy as np
import cv2 as cv


class Funcs:
    def __init__(self):
        with open("info.txt", "r", encoding="utf-8") as infos:
            infos = infos.read()
            print(infos)

    def screenshot(self):
        screen = pyaut.screenshot()
        screen = cv.cvtColor(np.array(screen), cv.COLOR_RGB2BGR)
        return screen

    def cut(self, screen):
        cropped_image = screen[720:1000, 40:350]
        return cropped_image

    def get_mon(self):
        for i in getm():
            print("\n {}".format(str(i)))

    def direction_determination(self, cropped_image):

        left_hard_vertices = np.array([[130, 210], [70, 150], [80, 100], [100, 90], [65, 95], [40, 155], [60, 220], [120, 215]])
        left_mid_vertices = np.array([[135, 205], [125, 125], [130, 90], [155, 80], [100, 90], [80, 100], [70, 150], [130, 210]])
        left_bit_vertices = np.array([[155, 80], [145, 90], [140, 200], [135, 205], [125, 125], [130, 90]])
        forward_vertices = np.array([[155, 80], [145, 90], [140, 200], [170, 200], [165, 90]])
        right_hard_vertices = np.array([[310 - 130, 210], [310 - 70, 150], [310 - 80, 100], [310 - 100, 90], [310 - 65, 95], [310 - 40, 155], [310 - 60, 220], [310 - 120, 215]])
        right_mid_vertices = np.array([[310 - 135, 205], [310 - 125, 125], [310 - 130, 90], [310 - 155, 80], [310 - 100, 90], [310 - 80, 100], [310 - 70, 150], [310 - 130, 210]])
        right_bit_vertices = np.array([[155, 80], [310 - 145, 90], [310 - 140, 200], [310 - 135, 205], [310 - 125, 125], [310 - 130, 90]])
        back_vertices = np.array([[135, 220], [310 - 135, 220], [310 - 120, 240], [120, 240]])
        u_left = np.array([[125, 225], [115, 220], [65, 225], [90, 250], [110, 245]])
        u_right = np.array([[310 - 125, 225], [310 - 115, 220], [310 - 65, 225], [310 - 90, 250], [310 - 110, 245]])

        def region_of_interest(img, vertices):
            mask = np.zeros_like(img)
            channel_count = img.shape[2]
            match_mask_color = (255,) * channel_count
            cv.fillPoly(mask, vertices, match_mask_color)
            masked_image = cv.bitwise_and(img, mask)
            return masked_image

        left_hard = region_of_interest(cropped_image, np.array([left_hard_vertices], np.int32))
        left_mid = region_of_interest(cropped_image, np.array([left_mid_vertices], np.int32))
        left_bit = region_of_interest(cropped_image, np.array([left_bit_vertices], np.int32))
        forward = region_of_interest(cropped_image, np.array([forward_vertices], np.int32))
        right_bit = region_of_interest(cropped_image, np.array([right_bit_vertices], np.int32))
        right_mid = region_of_interest(cropped_image, np.array([right_mid_vertices], np.int32))
        right_hard = region_of_interest(cropped_image, np.array([right_hard_vertices], np.int32))
        back = region_of_interest(cropped_image, np.array([back_vertices], np.int32))
        u_left_turn = region_of_interest(cropped_image, np.array([u_left], np.int32))
        u_right_turn = region_of_interest(cropped_image, np.array([u_right], np.int32))

        return left_hard, left_mid, left_bit, forward, right_bit, right_mid, right_hard, back, u_left_turn, u_right_turn