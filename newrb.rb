#!/usr/bin/env ruby

path = ARGV[0]
fail "specify filename to create" unless path

File.open(path,"w") {|f| f.puts "#!/usr/bin/env ruby -w"}
File.chmod(0755,path)
system "open",path