import sys
import datetime as dt

# date_str = sys.argv[1]
date_str = '22.12.1987'
b_date = dt.datetime.strptime(date_str, '%d.%m.%Y')
now = dt.datetime.now()

print(b_date.timestamp() * 1000)
# print(now.year - b_date.year)

delta = dt.timedelta(days=15)

new_date = now + delta
# print(b_date + delta)
print(new_date.strftime('%d %B %Y year, %H:%M'))

int_date = 567118800000

print(dt.datetime.fromtimestamp(int_date / 1000))