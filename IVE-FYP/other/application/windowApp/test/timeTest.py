import time
from datetime import datetime
ftime = datetime.strptime('18:24:01', '%H:%M:%S')
lTime = datetime.strptime('18:25:06', '%H:%M:%S')
timediff = lTime - ftime

print(timediff.seconds)
