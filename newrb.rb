#!/usr/bin/env ruby

path = ARGV[0]
fail "specify filename to create" unless path

File.open(path,"w") do |f| 
    f.puts "#!/usr/bin/env ruby"
    f.puts ""
    f.puts "#info"
    f.puts "#-name   : zhangruochi"
    f.puts "#-email  : zrc720@gmail.com"
end

File.chmod(0755,path)
system "open",path
