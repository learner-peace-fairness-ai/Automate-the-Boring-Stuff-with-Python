from datetime import datetime

print(datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.strptime("October of '15", "%B of '%y"))
print(datetime.strptime("November of '63", "%B of '%y"))
