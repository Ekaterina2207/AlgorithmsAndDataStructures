#Вычислите дату через 4 месяца от текущей даты

from datetime import datetime
from dateutil.relativedelta import relativedelta

given_date = datetime(2020, 2, 25).date()
found_date = given_date + relativedelta(months=4)

print(found_date)