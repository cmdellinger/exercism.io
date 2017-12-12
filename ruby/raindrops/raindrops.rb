# @title difference_of_squares
# @author cmdellinger
class Raindrops
  @@Raindrop_table = {3=> 'Pling',
                      5=> 'Plang',
                      7=> 'Plong'}
  # Generates a string of raindrops that contains a concatenation
  # of "Pling", "Plang", "Plong" if the integer has factors 3, 5, 7
  # respectively. If the integer has none of those factors, the
  # integer is returned as a string.
  #
  # @param input_number [Integer] number to be converted into "raindrops"
  # @return [String] a concatenation of "Pling", "Plang", and "Plong"
  #   for factors of 3, 5, 7 respectively. if no relevant factors,
  #   then passed number is returned as a string.
  def self.convert(input_number = 0)
      # check for relevant factors
      factors = @@Raindrop_table.keys.find_all {|integer| input_number%integer == 0}
      # return passed number if no relevant factors
      return input_number.to_s if factors.length == 0
      # build raindrops
      factors.collect{|factor| @@Raindrop_table[factor]}.reduce(:+)
  end
end

# BookKeeping Version
module BookKeeping
    # the version of the tests that are being run
    VERSION = 3
end
