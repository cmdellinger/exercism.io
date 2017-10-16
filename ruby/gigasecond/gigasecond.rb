# @title gigasecond
# @author cmdellinger
class Gigasecond
  # Adds a gigasecond (10^9 seconds) to the passed Time object.
  #
  #
  # @param time [Time] starting time to add a gigasecond to.
  # @return [Time] input time plus a gigasecond.
  def self.from(time = Time.now.utc)
    # Time + numeric -> Time
    time + 10**9
  end
end

# BookKeeping Version
module BookKeeping
    # the version of the tests that are being run
    VERSION = 6
end
