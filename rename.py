#!/usr/bin/env python3

# info
# -name   : zhangruochi
# -email  : zrc720@gmail.com

import os
import pathlib
import re
import sys

pattern = re.compile("[^\x00-\x7f]|\s")

for file in os.listdir("."):
    raw_path = pathlib.Path(file)
    new_path = pathlib.Path(re.sub(pattern,"",file))
    print("rename {} -> {}".format(raw_path,new_path))
    raw_path.rename(new_path)  

print("\nFinished!......")    


"""
for file in os.listdir("."):
    new_path = "".join([char for char in file if ord(char) < 128 ])
    print(new_path)
    os.system("mv {} {}".format(file,new_path))
"""
       

