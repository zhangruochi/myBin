#!/usr/bin/env ruby 

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


info = ARGV[0]
info = Time.now.to_s.split.first unless info

system "git add -A"
system "git commit -m #{info}"
system "git push -u origin master"


