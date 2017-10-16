# @title difference_of_squares
# @author cmdellinger

class Squares
  # Creates instance range sequence to be used in calculations.
  #
  # @param input_number [Integer] maximum of sequence from 1 to input_number.
  def initialize(input_number)
    @number_range = (1..input_number)
  end

  # Squares the sum of integers in the sequence of instance range.
  # Sequence range: 1 to input_number.
  #
  # @return [Integer] sum of the squares in object's range.
  def sum_of_squares
    @number_range.inject{|memo, n| memo + n**2}
  end
  
  # Squares the sum of integers in the sequence of instance range.
  # Sequence range: 1 to input_number.
  #
  # @return [Integer] sum of the squares in object's range.
  def square_of_sum
    @number_range.sum**2
  end
  
  # Calculates the difference between the square of sums and the sum of squares
  # for the instance range.
  #
  # @return [Integer] difference between the square of sums and the sum of squares.
  def difference
    # square of sums will always be bigger
    square_of_sum - sum_of_squares
  end
end

# BookKeeping Version
module BookKeeping
  # the version of the tests that are being run
  VERSION = 4 # Where the version number matches the one in the test.
end
