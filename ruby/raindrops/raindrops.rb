#### raindrops ####
#
#   Complement class with class method convert()
#       convert() takes in an integer and returns a string
#       of raindrops. The string contains a concatenation of
#       "Pling", "Plang", "Plong" if the integer has factors
#       3, 5, 7 respectively. If the integer has none of those
#       factors, the integer is returned as a string.
#
#   Raindrops.convert(<input_number>)
#
#   Parameters:
#       <input_number> : integer
#           any integer to be converted into "raindrops"
#
#   Returns:
#       <raindrops> : string
#           a concatenation of "Pling", "Plang", and "Plong"
#           for factors of 3, 5, 7 respectively. if no relevant
#           factors, then passed number is returned as a string.

class Raindrops
  @@Raindrop_table = {3=> 'Pling',
                      5=> 'Plang',
                      7=> 'Plong'}

  def self.convert(input_number = 0) #-> ""
      # check for relevant factors
      factors = @@Raindrop_table.keys.find_all {|integer| input_number%integer == 0}
      # return passed number if no relevant factors
      return input_number.to_s if factors.length == 0
      # build raindrops
      factors.collect{|factor| @@Raindrop_table[factor]}.reduce(:+)
  end
end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
  VERSION = 3 # Where the version number matches the one in the test.
end
