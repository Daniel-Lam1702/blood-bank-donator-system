import datetime
import random
start_date = datetime.date(datetime.date.today().year-64, 1, 1)
end_date = datetime.date(datetime.date.today().year-18, datetime.date.today().month, datetime.date.today().day-1)
hoy = datetime.date.today().year-64
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)
print(str(random_date)[8:]+"/"+str(random_date)[5:7]+"/"+str(random_date)[0:4])