import datetime
import pytz
today = datetime.date.today()
print(today)

birthday = datetime.date(1999, 9, 8)
print(birthday)

#find days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

# adding 10 days to current day
tdelta = datetime.timedelta(days = 10)
print(today - tdelta)

print(today.day)

# monday = 0, sunday = 6
print(today.weekday())
print(today.isoweekday())
print(today.month)
print(today.year)
print(today.min)
print(today.max)

print((datetime.time(8, 1, 50, 00)))
# print(datetime.date(y, m, d))
# print(datetime.time(h, m, s, ms ))
# print(datetime.datetime(y, m, d, h, m, s, ms))

#add 10 hours to the current day
hour_delta = datetime.timedelta(hours = 10)
print(datetime.datetime.now() + hour_delta)

print(datetime.datetime.now(tz = pytz.UTC))

datetime_today = datetime.datetime.now(tz = pytz.utc)
datetime_pacific = datetime_today.astimezone(pytz.timezone('us/pacific'))
print(datetime_pacific)
for tz in pytz.all_timezones:
    print(tz)

# string formatting with dates
# 2020-14-06 -> june 14, 2021

print(datetime_pacific.strftime('%B, %d, %Y'))

datetime_thing = datetime.datetime.strptime('June 14, 2021' , '%B %d, %Y')
print(datetime_thing)