#!/usr/bin/env python3

import os
import sys

fp = open(sys.argv[1],"w")
fp.write("#!/usr/bin/env python3\n")
fp.write("\n")
fp.write("#info\n")
fp.write("#-name   : zhangruochi\n")
fp.write("#-email  : zrc720@gmail.com\n")
fp.close()

os.system("chmod 755 {}".format(sys.argv[1]))
os.system("open {}".format(sys.argv[1]))

