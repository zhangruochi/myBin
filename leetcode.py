#!/usr/bin/env python3

import sys
from pathlib import PosixPath as P
import os



problem_name = sys.argv[1]
cur_work_dir = P("/Users/ZRC/Desktop/leetcode")
README_FILE =  cur_work_dir / "README.md"

cur_work_dir = cur_work_dir / problem_name

if not cur_work_dir.exists():
    (cur_work_dir).mkdir()
    (cur_work_dir/"solution.py").touch()
    (cur_work_dir/"solution.java").touch()
    (cur_work_dir/"solution.c++").touch()
    (cur_work_dir/"note.md").touch()

os.system("subl {}".format(cur_work_dir))
os.system("open {}".format(README_FILE))






