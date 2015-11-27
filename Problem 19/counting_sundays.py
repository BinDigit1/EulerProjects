import datetime
start_date = datetime.date(1900,1,1)
end_date = datetime.date(2000,12,31)

duration = end_date - start_date
for i in duration:
    print(i)