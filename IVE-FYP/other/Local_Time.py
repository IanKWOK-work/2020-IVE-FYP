import pytz
import datetime as dt
import geocoder
from pytz import reference

g = geocoder.ip('me')
print (g.city)

hktz = pytz.timezone('Asia/Hong_Kong')
print(dt.datetime.now(hktz).strftime('%Y-%m-%d %H:%M:%S'))

localtime = reference.LocalTimezone()
print (localtime.tzname(dt.datetime.now()))
print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))