# @title pangram
# @author cmdellinger
class Pangram
  # Determines whether a phrase is a pangram. A pangram is a
  # sentence that contains all the letters of the alphabet.
  #
  # @param phrase [String] sentence to be tested as a pangram.
  # @return [Boolean] true or false depending on pangram status.
  def self.pangram?(phrase)
    ('a'..'z').to_a == phrase.gsub(/[^a-zA-Z]/, '').downcase.split('').sort.uniq
  end
end

# BookKeeping Version
module BookKeeping
   # the version of the tests that are being run
   VERSION = 5
end
