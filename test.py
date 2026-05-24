from enum import Flag, auto

class DaysOfWeek(Flag):
    Monday=auto()
    Tuesday=auto()
    Wednesday=auto()
    Thursday=auto()
    Friday=auto()
    Saturday=auto()
    Sunday=auto()

for i in range(len(DaysOfWeek)):
    print(i)
    day_of_week = DaysOfWeek(2**i)
    print(day_of_week)
    #print(day_of_week)
    #print(day_of_week.value)
    #print(day_of_week in DaysOfWeek(b))
#print((1) in DaysOfWeek(1+2))