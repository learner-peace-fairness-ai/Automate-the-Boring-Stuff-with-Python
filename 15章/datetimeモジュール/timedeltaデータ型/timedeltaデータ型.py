from datetime import timedelta

delta = timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(delta)
