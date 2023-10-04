#!/usr/bin/env ruby
# This ruby script accepts one argument and passes it to a 
# regular expression matching method
# The below regular expression matches a 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
