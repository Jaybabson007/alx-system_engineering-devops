#!/usr/bin/env ruby
# This ruby script accepts one argument and passes it to a regular,
# expression matching method
# The below regular expression matches School

puts ARGV[0].scan(/School/).join
