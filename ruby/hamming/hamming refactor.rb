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
        # actual comparison: breaks strings into arrays and compares elements
        return string1.chars.zip(string2.chars).count {|s1, s2| s1 != s2}
    end
end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
    VERSION = 3 # Where the version number matches the one in the test.
end
