#!/usr/bin/env ruby
require 'csv'

if ARGV.length < 1
  puts "Usage: $0 file.csv"
end

input_file = ARGV[0]

puts "[list]"
CSV.foreach(input_file) do |entries|
  entries[1] = "[i]" + entries[1] + "[/i]" unless entries[1].nil?
  entries[3] = "(" + entries[3] + ")" unless entries[3].nil?
  puts "[*]" + entries.join(" ")
end
puts "[/list]"
