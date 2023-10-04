#!/usr/bin/env ruby
# This ruby script accepts one argument and passes it to a 
# regular expression matching method
# The below regular expression matches the given cases

puts ARGV[0].scan(/hbt{2,5}n/).join
