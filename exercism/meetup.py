''' exercise meetup '''

from calendar import monthrange
from datetime import date

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

days_of_week_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                     'Friday': 4, 'Saturday': 5, 'Sunday': 6}

weeks_dict = {'first': 1, 'second': 8, 'third': 15, 'fourth': 22, 'fifth': 29,
              'last': -6, 'teenth': 13}

def meetup(year, month, week, day_of_week):
    day_of_week = days_of_week_dict[day_of_week]
    week = weeks_dict[week.lower()]
    first_day_type, days_count  = monthrange(year, month)
    if week < 0:
        week += days_count
    if first_day_type == day_of_week:
        counted_day = 1
    elif first_day_type < day_of_week:
        counted_day = 1 + day_of_week - first_day_type
    else:
        counted_day = 8 - first_day_type + day_of_week 
    while counted_day < week and counted_day < days_count:
        counted_day += 7
    if counted_day > days_count or not (week <= counted_day < week + 7):
        raise MeetupDayException("That day does not exist.")
    return date(year, month, counted_day)
    
    
if __name__ == '__main__':
    print(meetup(2022, 2, 'fifth', 'Monday'))
