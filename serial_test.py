#! /usr/bin/env python
# coding: utf-8
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)


def serial_monitor():
    pass

if __name__ == '__main__':
    serial_monitor()
