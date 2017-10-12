#### pangram ####
#
#   Pangram class with class method pangram?()

class Pangram
  def self.pangram?(phrase) #-> boolean
    ('a'..'z').to_a == phrase.gsub(/[^a-zA-Z]/, '').downcase.split('').sort.uniq
  end
end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
    VERSION = 5 # Where the version number matches the one in the test.
end
