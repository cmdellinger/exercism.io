"""
Exercism.io assignment - meetup.py
written by (GitHub):     cmdellinger

Usage:
    meetup.py year <year> month <month> weekday <weekday> position <position>

Returns the meetup date for the given year, month, weekday, and position.
Positions accepted include ordinal (1st, 2nd, ...), first, last, teenth.
"""

## ------
## Exercism.io function
## ------

from calendar import monthrange
from datetime import date

def meetup_day(year = 0000, month = 00,
               day = 'weekday', position = 'ordinal#'): #-> date(year,month,day)

    # get number of days in the given month
    first_day, days_in_month = monthrange(year,month)
    # get all date in the month that corespond to the given weekday
    weekday_dates = [day_of_month for day_of_month in xrange(1, days_in_month + 1)
                     if date(year, month, day_of_month).strftime('%A') == day]

    # generate ordinal numbers for quantity of weekdays in month
    # ordinal lambda function form stackoverflow ( https://stackoverflow.com/a/20007730 )
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    ordinals_for_weekday = {ordinal(n): index for index, n in enumerate(range(1,len(weekday_dates)+1))}

    # create index key for position
    index_key = {'first': 0, 'last': -1}
    index_key.update(ordinals_for_weekday)
    index_key['teenth'] = weekday_dates.index([x for x in weekday_dates if x in xrange(13,20)][0])
    
    return date(year, month, weekday_dates[index_key[position]])

## ------
## Command-line implementation
## ------

if __name__ == '__main__':
    from docopt import docopt
    
    meetup_date = meetup_day(int(docopt(__doc__)['<year>']), int(docopt(__doc__)['<month>']),
                             docopt(__doc__)['<weekday>'], docopt(__doc__)['<position>'])
    print 'meetup date: {}'.format(meetup_date)
