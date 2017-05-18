#!/usr/bin/env ruby -w

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com


app_name = ARGV[0]
puts "open the application #{app_name}"
system "open","/Applications/#{app_name}.app"
