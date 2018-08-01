# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))
dt = datetime(2017, 8, 11, 23, 34)
print(dt)
print(dt.timestamp())
t = dt.timestamp()
print(datetime.fromtimestamp(t))
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=2,hours=12))

tz_utc_8 = timezone(timedelta(hours=8))

now = datetime.now()
print(now)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

#dt_str = input('please input time str : ')
#tz_str = input('please input utc : ')

def to_timestamp(dt_str, tz_str):
    time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print(time.timestamp())
    hr = re.match(r'^UTC\+(\d{1,2})\:00$', 'UTC+7:00').group(1)
    #realTime = time + (timedelta(hours=int(hr)))
    tz = timezone(timedelta(hours=int(hr)))
    time = time.replace(tzinfo=tz)
    print(time.timestamp())

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
