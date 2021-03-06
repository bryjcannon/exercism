from datetime import date
from calendar import Calendar

def meetup_day(year, month, name, ordinal):
    
    wkday_dict = {'Monday':0, 'Tuesday':1,
                  'Wednesday':2, 'Thursday':3,
                  'Friday':4, 'Saturday':5, 
                  'Sunday':6
                  }
    wkday = wkday_dict[name]
    
    cal = Calendar()
    date_list = []
    
    for day_date, weekday in cal.itermonthdays2(year, month):
        if weekday == wkday and not day_date == 0:
            date_list.append(day_date)
    
    date_dict = {'1st':0, '2nd':1, '3rd':2, '4th':3, '5th':4}
    if ordinal in date_dict:
        day = date_list[date_dict[ordinal]]
    elif ordinal == 'teenth':
        for day_date in date_list:
            if 12 < day_date < 20:
                day = day_date
    elif ordinal == 'last':
        day = date_list[-1]
                    
    
    return date(year, month, day)
