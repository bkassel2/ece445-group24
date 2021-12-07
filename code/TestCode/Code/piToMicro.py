#!/usr/bin/env python3
import serial
# if __name__ == '__main__':
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.baudrate = 9600
ser.reset_input_buffer()
# ser.close()
# ser.open()
while True:
    # try:
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    # except:
    #     pass