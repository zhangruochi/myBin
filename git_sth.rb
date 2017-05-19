#!/usr/bin/env ruby 

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


info = ARGV.join(" ")
info = Time.now.to_s.split.first if info.length == 0

system "git add -A"
system "git commit -m #{info}"
system "git push -u origin master"


