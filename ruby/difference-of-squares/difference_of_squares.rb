#### difference_of_squares ####
#
#   Squares class
#
#   Instance Methods:
#     new(<input_number>)
#       initializes instance with number to be used in calculations
#
#     sum_of_squares()
#       returns sum of squares
#
#     square_of_sum()
#       returns square of sums
#
#     difference()
#       returns difference between square of sums and sum of squares
#
#     accessor methods: number
#       change or check value of input number


class Squares
  attr_accessor :number

  def initialize(input_number)
    @number = input_number
  end

  def sum_of_squares
    (1..@number).inject{|memo, n| memo + n**2}
  end
  
  def square_of_sum
    (1..@number).sum**2
  end
  
  def difference
    # square of sums will always be bigger
    square_of_sum - sum_of_squares
  end
end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
  VERSION = 4 # Where the version number matches the one in the test.
end
