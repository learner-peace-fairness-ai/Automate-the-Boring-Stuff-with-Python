from datetime import datetime
from datetime import timedelta

dt = datetime.now()
print(dt)

thousand_days = timedelta(days=1000)
print(dt + thousand_days)

oct21st = datetime(2015, 10, 21, 16, 29, 0)
about_thirty_years = timedelta(days=365 * 30)

print(oct21st)
print(oct21st - about_thirty_years)
print(oct21st - (2 * about_thirty_years))
