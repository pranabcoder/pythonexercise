import time
import calendar

# print(time.localtime())
local_time = time.asctime(time.localtime(time.time()))
# print(local_time)

day_value = calendar.weekday(1947, 8, 15)
print(calendar.day_name[day_value])

