#!/usr/bin/env ruby
require 'date'

start_date = Date.new(2012,7,14)
end_date = Date.today

puts (start_date..end_date).to_a.select { |d| d.friday? }.reverse
