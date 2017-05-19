#!/usr/bin/env ruby 

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


time = Time.now.to_s.split.first


system "git add -A"
system "git commit -m #{time}"
system "git push -u origin master"


