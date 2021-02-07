"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


Population = int(input("Enter the population:"))
Doses_ad = int(input("Enter the number of doses administered:"))
Doses_perday = int(input("Enter the number of doses administered per day:"))
if Doses_ad%2 == 0:
    People_vacc = Doses_ad/2
else:
    People_vacc = (round(Doses_ad/2))-1
People_needed = Population*0.8
People_remaining = People_needed - (People_vacc)
People_vacc1day = Doses_perday/2
No_of_days = People_remaining/People_vacc1day
today:datetime = datetime.today()
req_day: timedelta = timedelta(No_of_days)
final_day: datetime = today + req_day
print("Population", Population)
print("Doses administered:", Doses_ad)
print("Doses per day:", Doses_perday)
print("Target percent vaccinated: 80%")
print("We will reach 80% vaccination in", round(No_of_days),"days, which falls on", final_day.strftime("%B %d, %Y"))
