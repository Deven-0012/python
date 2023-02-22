import datetime

mytime = datetime.time(14,44,14,2)
print(mytime.hour)
print(mytime.minute)
print(mytime.second)
print(mytime.microsecond)

mydate = datetime.date.today()
print(mydate)
print(mydate.day)


from datetime import datetime

mydatetime = datetime(2023,7,1,0,1,1)
print(mydatetime)