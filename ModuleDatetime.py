import datetime as dt
#
#
# print("-----------  #1 Let's figure out the duration of our favorite series ----------")
#
# start_time = dt.datetime(2011, 4, 17)
# print(f'Start time is {start_time}')
#
# final_time = dt.datetime(2018, 6, 20)
# print(f'Final time is {final_time}')
#
# duration = final_time - start_time
#
# print(f'Total duration is {duration}')
#
#
# print("----------- #2 Find out exact time of Haharin in space ----------")
#
# start_time = dt.datetime(1961, 4, 12, 9, 7, 0)
# landing_time = dt.datetime(1961, 4, 12, 10, 55, 0)
# print(f'Yurii Haharin was in space for {landing_time - start_time}')
#
# import datetime as dt
#
#
# start_moment = dt.datetime(2020, 9, 1)  # напишите код здесь
# current_moment = dt.datetime(2020, 10, 16)
#
# total_time = current_moment - start_moment
#
# print(total_time)
#
# print("----------- #3 Discover how are you old exactly  right now ?! ----------")
# my_bithday = dt.datetime(1992, 8, 24, 4)
# print(f'my bithday is {my_bithday}')
# current_day = dt.datetime(2020, 10, 18, 15, 47)
# print(f'Today is {current_day}')
# my_accurate_age = current_day - my_bithday
# print(f'My accurate age is {my_accurate_age}')


print("----------- Standart UTC [Coordinated Universal Time] ----------")

print("Print General Coordinated Universal Time")
now = dt.datetime.utcnow()
print(now)

print("Print Coordinated Universal Time in your region e.g. In Kyiv, Ukraine - it is UTC+3 hours")
region_difference = dt.timedelta(hours=3)
kyiv_time = now + region_difference
print(kyiv_time)


print("----------- 2019 Formula 1 World Championship Australian Grand Prix winner, Valtteri Bottas completed his fastest lap in 1 "
      "minute 25 seconds and 273,250 microseconds. The second result was shown by Lewis Hamilton with a difference of "
      "208860 microseconds. Let's calculate the time of Hamilton's fastest lap.-------------- ")

time_bottas = dt.timedelta(minutes=1, seconds=25,
                           microseconds=273250)

time_bottas = dt.timedelta(minutes=1, seconds=25,
                           microseconds=273250)
time_hamilton = time_bottas + dt.timedelta(microseconds=208860)
print(time_hamilton)
