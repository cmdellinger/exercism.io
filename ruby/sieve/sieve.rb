# @title sieve
# @author cmdellinger
class Sieve
  # @param input_number [Integer] maximum of range to be tested for primes.
  def initialize(input_number)
    @number = input_number
  end
  
  # Finds primes up to the instance number using the Sieve of
  # Eratosthenes algorithm.
  #
  # @return [Array] prime values in range 2 to instance number.
  def primes()
    return [] if @number < 2
    # build Boolean array to use for sieve with buffer to align indices
    sieve_array = Array.new(2, false) + Array.new(@number-1, true)
    # perform Sieve of Eratosthenes eliminations
    (2..Math.sqrt(@number).to_i).each do |i|
        (i**2..@number).step(i) {|j| sieve_array[j] = false} if sieve_array[i] == true
    end
    # return numbers by corresponding index that are still true
    (2..@number).collect {|index| index if sieve_array[index] == true}.compact
  end
end

# BookKeeping Version
module BookKeeping
    # the version of the tests that are being run
    VERSION = 1
end
