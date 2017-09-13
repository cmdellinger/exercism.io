#### hamming ####
#
#   Hammming class with compute method
#

class Hamming
    def self.compute(string1 = "", string2 = "")
        # check that strings are the same length
        unless string1.length == string2.length
            raise ArgumentError.new("Sequences must be equal in length.")
        end
        # compute hamming distance
        distance = 0 #initialize to zero
        # iterate over string and compare each letter stepwise
        0.upto(string1.length) do |i|
            distance += (string1[i] == string2[i] ? 0 : 1)
        end
        return distance
    end
end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
    VERSION = 3 # Where the version number matches the one in the test.
end
