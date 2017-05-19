#!/usr/bin/env ruby -w

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


time = Time.now

system "git add -A"
system "git commit -m #{time}"
system "git push -u origin master"


