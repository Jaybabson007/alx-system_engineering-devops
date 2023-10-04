#!/usr/bin/env ruby
# This ruby script accepts one argument and passes it to a
# regular expression matching method
# This ruby script outputs: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
