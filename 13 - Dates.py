from datetime import datetime

now = datetime.now()

print('fecha: ',now.day,'.', now.month,'.',now.year)
print('Hora: ', now.hour,':',now.minute,':', now.second)

timestamp = now.timestamp()

print(now)
print(timestamp) 
print(datetime)

from datetime import time

current_time = time(now.hour,now.minute,now.second)

print(current_time)

import time
current_time_2 = time.localtime()

hora_actual = time.strftime("%H:%M:%S", current_time_2)
print("La hora actual es:", hora_actual)

print(hora_actual)

from datetime import timedelta

star_delta = timedelta(10,5,6)
print(star_delta)