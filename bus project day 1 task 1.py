# importing date from date time module.
from datetime import date
date = date.today()


def find_day():
    # get today's date

    day = date.strftime("%a")

    if(day == 'Sat'):
        print('Date: ', date)
        print('Day: ', day)
        print('Fare: 60')
    elif(day == 'Sun'):
        print('Date: ', date)
        print('Day: ', day)
        print('Fare: 800')
    else:
        print('Date: ', date)
        print('Day: ', day)
        print('Fare: 100')


find_day()