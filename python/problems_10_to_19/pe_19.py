day_of_week=3
count=0

for year in range(1,101):
    for month in range(1,13):
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            day_of_week=day_of_week+31

        elif month==2:
            if year%4==0:
                day_of_week=day_of_week+29
            else:
                day_of_week=day_of_week+28
        elif month==4 or month==6 or month==9 or month==11:
            day_of_week=day_of_week+30
        
        day_of_week=day_of_week%7

        if day_of_week==0:
            count=count+1

print(count)