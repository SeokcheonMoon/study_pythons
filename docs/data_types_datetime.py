# datatime은 일시증가 방식

from datetime import datetime

start_time = datetime.now()
now = datetime.now()
pass

first_date = datetime(2023,12,20)
# datetime.datetime(2023, 12, 20, 0, 0)

second_date = datetime.strptime("2023-12-25","%Y-%m-%d")
# datetime.datetime(2023, 12, 25, 0, 0)


#2023-12-20 - 2023-12-25
result_date = first_date - second_date

end_time = datetime.now()

e_s_time = end_time - start_time

pass