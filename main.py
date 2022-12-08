# importing libs
import cv2
import funcs
import numpy as np
import time
from playsound import playsound

# Test and more tests...
"""Fun.get_mon()
screen = Fun.screenshot()
cropped_screen = Fun.cut(screen)

cv.imshow("screen",cropped_screen)

cv.waitKey(0)
cv.destroyAllWindows()"""

# setups and setup
Fun = funcs.Funcs()
l_hard_num = 0
l_mid_num = 0
l_bit_num = 0
forward_num = 0
r_bit_num = 0
r_mid_num = 0
r_hard_num = 0
back_num = 0
u_left_num = 0
u_right_num = 0
language_choice = str(input(" Choose the language (write EN or TR):  "))

# main function (loop)
while True:
    try:
        # preparing frame
        screen = Fun.screenshot()
        cropped_screen = Fun.cut(screen)
        l_hard, l_mid, l_bit, forward, r_bit, r_mid, r_hard, back, u_left, u_right = Fun.direction_determination(cropped_screen)

        # defining color
        blue_lower = np.array([180, 160, 0])
        blue_upper = np.array([255, 255, 150])

        # finding the range blue color in the screen
        l_hard_mask = cv2.inRange(l_hard, blue_lower, blue_upper)
        l_mid_mask = cv2.inRange(l_mid, blue_lower, blue_upper)
        l_bit_mask = cv2.inRange(l_bit, blue_lower, blue_upper)
        forward_mask = cv2.inRange(forward, blue_lower, blue_upper)
        r_bit_mask = cv2.inRange(r_bit, blue_lower, blue_upper)
        r_mid_mask = cv2.inRange(r_mid, blue_lower, blue_upper)
        r_hard_mask = cv2.inRange(r_hard, blue_lower, blue_upper)
        back_mask = cv2.inRange(back, blue_lower, blue_upper)
        u_left_mask = cv2.inRange(u_left, blue_lower, blue_upper)
        u_right_mask = cv2.inRange(u_right, blue_lower, blue_upper)
        z = 0

        if z == 1:
            continue
        elif z == 0:
            for i in l_hard_mask:
                if i.any() != 0:
                    if l_hard_num == 1:
                        z = 1
                        continue
                    elif l_hard_num == 0:
                        l_hard_num = 1
                        l_mid_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/l_hard.mp3'.format(language_choice))

        if z == 1:
            continue
        elif z == 0:
            for i in l_mid_mask:
                if i.any() != 0:
                    if l_mid_num == 1:
                        z = 1
                        continue
                    elif l_mid_num == 0:
                        l_mid_num = 1
                        l_hard_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/l_mid.mp3'.format(language_choice))

        if z == 1:
            continue
        elif z == 0:
            for i in l_bit_mask:
                if i.any() != 0:
                    if l_bit_num == 1:
                        z = 1
                        continue
                    elif l_bit_num == 0:
                        l_bit_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/l_bit.mp3'.format(language_choice))


        if z == 1:
            continue
        elif z == 0:
            for i in forward_mask:
                if i.any() != 0:
                    if forward_num == 1:
                        z = 1
                        continue
                    elif forward_num == 0:
                        forward_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        l_bit_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/forward.mp3'.format(language_choice))


        if z == 1:
            continue
        elif z == 0:
            for i in r_bit_mask:
                if i.any() != 0:
                    if r_bit_num == 1:
                        z = 1
                        continue
                    elif r_bit_num == 0:
                        r_bit_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/r_bit.mp3'.format(language_choice))


        if z == 1:
            continue
        elif z == 0:
            for i in r_mid_mask:
                if i.any() != 0:
                    if r_mid_num == 1:
                        z = 1
                        continue
                    elif r_mid_num == 0:
                        r_mid_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/r_mid.mp3'.format(language_choice))


        if z == 1:
            continue
        elif z == 0:
            for i in r_hard_mask:
                if i.any() != 0:
                    if r_hard_num == 1:
                        z = 1
                        continue
                    elif r_hard_num == 0:
                        r_hard_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        back_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/r_hard.mp3'.format(language_choice))


        if z == 1:
            continue
        elif z == 0:
            for i in back_mask:
                if i.any() != 0:
                    if back_num == 1:
                        z = 1
                        continue
                    elif back_num == 0:
                        back_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        u_left_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/back.mp3'.format(language_choice))


        if z == 1:
            continue
        elif z == 0:
            for i in u_left_mask:
                if i.any() != 0:
                    if u_left_num == 1:
                        z = 1
                        continue
                    elif u_left_num == 0:
                        u_left_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_right_num = 0
                        playsound('Voice(Ses)/{}/u_left.mp3'.format(language_choice))


                    
        if z == 1:
            continue
        elif z == 0:
            for i in u_right_mask:
                if i.any() != 0:
                    if u_right_num == 1:
                        z = 1
                        continue
                    elif u_right_num == 0:
                        u_right_num = 1
                        l_hard_num = 0
                        l_mid_num = 0
                        l_bit_num = 0
                        forward_num = 0
                        r_bit_num = 0
                        r_mid_num = 0
                        r_hard_num = 0
                        back_num = 0
                        u_left_num = 0
                        playsound('Voice(Ses)/{}/u_right.mp3'.format(language_choice))

        # showing result (optional)
        """cv2.imshow("original", cropped_screen)
        cv2.imshow("masked", mask)
        cv2.imshow("l_h", l_hard)
        cv2.imshow("l_m", l_mid)
        cv2.imshow("l_b", l_bit)
        cv2.imshow("f", forward)
        cv2.imshow("r_b", r_bit)
        cv2.imshow("r_m", r_mid)
        cv2.imshow("r_h", r_hard)
        cv2.imshow("b", back)
        cv2.imshow("u_r", u_right)
        cv2.imshow("u_l", u_left)
        cv2.imshow("l_h_masked", l_hard_mask)
        cv2.imshow("l_m_masked", l_mid_mask)
        cv2.imshow("l_b_masked", l_bit_mask)
        cv2.imshow("f_masked", forward_mask)
        cv2.imshow("r_b_masked", r_bit_mask)
        cv2.imshow("r_m_masked", r_mid_mask)
        cv2.imshow("r_h_masked", r_hard_mask)
        cv2.imshow("b_masked", back_mask)
        cv2.imshow("u_r_masked", u_right_mask)
        cv2.imshow("u_l_masked", u_left_mask)"""


        # exiting from loop if we requires
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        # adding delay
        time.sleep(0.1)

    except:
        print("somethings wrong, i can feel it...")
        time.sleep(4)


cv2.destroyAllWindows()
