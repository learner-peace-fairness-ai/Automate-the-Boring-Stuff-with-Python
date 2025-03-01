from datetime import datetime

helloween2015 = datetime(2015, 10, 31, 0, 0, 0)
newyears2016  = datetime(2016, 1, 1, 0, 0, 0)
oct31_2015    = datetime(2015, 10, 31, 0, 0, 0)

print(helloween2015 == oct31_2015)
print(helloween2015 > newyears2016)
print(newyears2016 > helloween2015)
print(newyears2016 != oct31_2015)
