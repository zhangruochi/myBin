#!/usr/bin/env ruby

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com

require "timeout"
require 'net/ssh'
require 'net/scp'

IP = "59.72.109.192"
USER = "zhangruochi"
PASS = "lv23623600"


para = ARGV[0]
dir = ARGV[1]


Net::SCP.start(IP,USER,password: PASS) do |scp|
    if para == "u"
        scp.upload! dir, "upload",{recursive: true}
        puts "upload successul......."
    elsif para == "d"
        scp.download! dir,"download",{recursive: true}
        puts "download successul......"
    else
        puts "parameter error"
    end
end    





