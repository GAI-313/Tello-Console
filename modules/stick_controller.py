# -*- coding: utf-8 -*-

from tello import console
from rc import procon
import time
import sys
import cv2
import re

class procon_console:
    def __init__(self):
        self.rc_res = procon()
        self.drone = console()
        self.button_response = None

        if self.drone.error_msg is True:
            pass

    def read(self):
        button, stick = self.rc_res.read()

        self.drone.rc(stick[2], stick[3], stick[1], stick[0])

        self.button_response = button
        b_res = self.button_response

        if "quit" in b_res:
            print("Done")
            sys.exit()

        if "home" in b_res:
            self.drone.land()

        if "func_right_stick" and  "func_left_stick" in b_res:
            time.sleep(1)
            self.drone.motor_start()

    def takeoff_land(self, tof):
        int_tof = re.sub(r"\D", "", tof)

        if int(int_tof) <= 100:
            time.sleep(1)
            while True:
                t = self.drone.takeoff()
                if t == "None response":
                    continue
                else:
                    break

        else:
            self.drone.land()

    def closer(self):
        cv2.destroyAllWindows()
        self.drone.cap.release()

procon = procon_console()

while True:
    procon.read()
