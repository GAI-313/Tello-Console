# -*- coding: utf-8 -*-

import hid
import time
import sys


def write_output_report(device, pkn, cmd, scmd, arg):
    device.write(cmd
                + pkn.to_bytes(1, byteorder='big')
                + b'\x00\x01\x40\x40\x00\x01\x40\x40'
                + scmd
                + arg)

def get_nbit_from_input_report(input_report, offset_byte, offset_bit, nbit):
    return (input_report[offset_byte] >> offset_bit) & ((1 << nbit) - 1)

def get_button_down(input_report):
    return get_nbit_from_input_report(input_report, 5, 0, 1)

def get_button_up(input_report):
    return get_nbit_from_input_report(input_report, 5, 1, 1)

def get_button_right(input_report):
    return get_nbit_from_input_report(input_report, 5, 2, 1)

def get_button_left(input_report):
    return get_nbit_from_input_report(input_report, 5, 3, 1)

def get_button_ZL(input_report):
    return get_nbit_from_input_report(input_report, 5, 7, 1)

def get_button_L(input_report):
    return get_nbit_from_input_report(input_report, 5, 6, 1)

def get_button_ZR(input_report):
    return get_nbit_from_input_report(input_report, 3, 7, 1)

def get_button_R(input_report):
    return get_nbit_from_input_report(input_report, 3, 6, 1)

def get_button_A(input_report):
    return get_nbit_from_input_report(input_report, 3, 3, 1)

def get_button_B(input_report):
    return get_nbit_from_input_report(input_report, 3, 2, 1)

def get_button_X(input_report):
    return get_nbit_from_input_report(input_report, 3, 1, 1)

def get_button_Y(input_report):
    return get_nbit_from_input_report(input_report, 3, 0, 1)

def get_button_min(input_report):
    return get_nbit_from_input_report(input_report, 4, 0, 1)

def get_button_plus(input_report):
    return get_nbit_from_input_report(input_report, 4, 1, 1)

def get_button_rs(input_report):
    return get_nbit_from_input_report(input_report, 4, 2, 1)

def get_button_ls(input_report):
    return get_nbit_from_input_report(input_report, 4, 3, 1)

def get_button_home(input_report):
    return get_nbit_from_input_report(input_report, 4, 4, 1)

def get_button_select(input_report):
    return get_nbit_from_input_report(input_report, 4, 5, 1)

def get_stick_l_h(input_report):
    return get_nbit_from_input_report(input_report, 6, 0, 8) | (get_nbit_from_input_report(input_report, 7, 0, 4) << 8)

def get_stick_l_v(input_report):
    return get_nbit_from_input_report(input_report, 7, 4, 4) | (get_nbit_from_input_report(input_report, 8, 0, 8) << 4)

def get_stick_r_h(input_report):
    return get_nbit_from_input_report(input_report, 9, 0, 8) | (get_nbit_from_input_report(input_report, 10, 0, 4) << 8)

def get_stick_r_v(input_report):
    return get_nbit_from_input_report(input_report, 10, 4, 4) | (get_nbit_from_input_report(input_report, 11, 0, 8) << 4)

class procon:
    def __init__(self):
        self.err = False
        try:
            v_ID = 0x057E
            p_ID = 0x2009

            self.device = hid.device()
            self.device.open(v_ID, p_ID) # paiering Pro controller

            time.sleep(0.02) # cool time

            write_output_report(self.device, 1, b'\x01', b'\x03', b'\x30')

        except OSError:
            print("Controller is not connection !\nV2")
            self.err = True

    def read(self):
        '''
        read = button_status, stick_status
        button_status = drone.rc[2,3,1,0]
        '''
        if self.err is False:
            input_report = self.device.read(49)              
            
            # Detect button
            button_status = '{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}'.format("flip_back"          if get_button_down(input_report) else "",
                                                                                            "flip_forward"      if get_button_up(input_report) else "",
                                                                                            "flip_right"        if get_button_right(input_report) else "",
                                                                                            "flip_left"         if get_button_left(input_report) else "",
                                                                                            "camera_angle"      if get_button_L(input_report) else "",
                                                                                            "take_pic"          if get_button_R(input_report) else "",
                                                                                            "func_1"            if get_button_ZR(input_report) else "",
                                                                                            "func_2"            if get_button_ZL(input_report) else "",
                                                                                            "func_A"            if get_button_A(input_report) else "",
                                                                                            "func_B"            if get_button_B(input_report) else "",
                                                                                            "quit"              if get_button_X(input_report) else "",
                                                                                            "yes"               if get_button_Y(input_report) else "",
                                                                                            "func_m"            if get_button_min(input_report) else "",
                                                                                            "func_p"            if get_button_plus(input_report) else "",
                                                                                            "func_right_stick"  if get_button_rs(input_report) else "",
                                                                                            "func_left_stick"   if get_button_ls(input_report) else "",
                                                                                            "home"              if get_button_home(input_report) else "",
                                                                                            "select"            if get_button_select(input_report) else "")
            # stick
            stick_status = [get_stick_l_h(input_report) // 10 -200, get_stick_l_v(input_report) // 10 -200, get_stick_r_h(input_report) // 10 -200, get_stick_r_v(input_report) // 10 -200]
            
            return button_status, stick_status
        else:
            print("read methot is can't running. please connect the controller and restart program V2")
            sys.exit()
