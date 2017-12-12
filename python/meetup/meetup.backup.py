from calendar import monthrange
from calendar import day_name
from itertools import islice
from datetime import date

# modified cycle from stackoverflow ( https://stackoverflow.com/a/8942392 )
def cycle(my_list, start_at=None):
    start_at = 0 if start_at is None else my_list.index(start_at)
    while True:
        yield my_list[start_at]
        start_at = (start_at + 1) % len(my_list)

def meetup_day(year = 0000, month = 00, day = 'weekday', position = 'ordinal#'): #-> date(year,month,day)
    # "Monday" = 0..."Sunday" = 6
    weekday2num = {key: value for value, key in enumerate(day_name)}
    num2weekday = dict(enumerate(day_name))
    # generate month data
    # format: [(day of month, 'Weekday'), ...]
    first_day, days_in_month = monthrange(year,month)
    month_days = [(i+1, num2weekday[key]) for i, key in enumerate(islice(cycle(range(0,7),first_day), days_in_month))]
    # sort days of month by weekday
    # format: {'Weekday': [day1,day8], ...}
    weekday_days = {}
    for day_of_month, week_day in month_days:
        try:
            weekday_days[week_day].append(day_of_month)
        except:
            weekday_days[week_day] = [day_of_month]
    # generate ordinal numbers for quantity of weekdays in month
    # ordinal lambda function form stackoverflow ( https://stackoverflow.com/a/20007730 )
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    ordinals_for_weekday = {ordinal(n): index for index, n in enumerate(range(1,len(weekday_days[day])+1))}
    # index key for position
    index_key = {'first': 0, 'last': -1}
    index_key.update(ordinals_for_weekday)
    index_key['teenth'] = weekday_days[day].index([x for x in weekday_days[day] if x in xrange(13,20)][0])
    return date(year, month, weekday_days[day][index_key[position]])
