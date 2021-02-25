#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
import locale
from datetime import datetime, date, timedelta
dt = date.today()
print(dt)
delta = timedelta(1)
print(dt - delta)
delta = timedelta(days=30)
print(dt - delta)

#Превратите строку "01/01/25 12:10:03.234567" в объект datetime
date_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
#2025-01-01 12:10:03.234567

