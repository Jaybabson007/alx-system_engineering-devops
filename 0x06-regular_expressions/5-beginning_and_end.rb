#!/usr/bin/env ruby
# This ruby script accepts one argument and passes it to a
# regular expression matching method
# The below regular expression matches a string that starts
# with h ends with n and can have any other single character in between

puts ARGV[0].scan(/^h.n$/).join
