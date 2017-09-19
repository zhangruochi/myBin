#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com


import time
import os
import sys
from sys import argv



def count_down(min):

    current_time = int(min) * 60
    while True: 
        current_time = current_time - 1
        sys.stdout.write(convert(current_time))
        sys.stdout.flush()

        time.sleep(1)
        if current_time == 0:
            os.system("say time is over")
            break

def convert(second):
    min = str(second // 60)
    sec = str(second % 60)

    if len(min) == 1:
        min = "0" + min

    if len(sec) == 1:
        sec = "0" + sec


    return "{}:{}\b\b\b\b\b".format(min,sec)


if __name__ == '__main__':
    count_down(argv[1])

      

