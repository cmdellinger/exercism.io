#### gigasecond ####
#
#   Gigasecond class with class method from()
#       from() adds a gigaescond or 10^9 seconds to
#       the time that was passed into it. if nothing
#       is passed, it defaults to now.
#
#   Usage:
#       Gigasecond.from(<Time instance>)
#
#   Output: Time instance

class Gigasecond
    def self.from(time = Time.now.utc)
        # Time + numeric -> Time
        return time + 10**9
    end
end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
    VERSION = 6 # Where the version number matches the one in the test.
end
