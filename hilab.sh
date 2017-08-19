#!/usr/bin/expect            

#info
#-name   : zhangruochi
#-email  : zrc720@gmail.com       

set timeout 3                       
spawn ssh zhangruochi@59.72.109.192 
expect "zhangruochi@59.72.109.192's password:"                 
send "lv23623600\r"                
#send "sudo -s\r" 
interact                          