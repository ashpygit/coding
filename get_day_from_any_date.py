date_input=input("Enter any date in the format(dd-mm-yyyy): ")

date_day = date_input[:2]
date_month = date_input[3:5] 
date_year=date_input[6:10]

year_code=int(((int(date_year[2:])) + (int(date_year[2:])/4))%7)
month_code=0
century_code=0
leap_year_code=0
date_day_of_week=''

match date_month:
    case '01':
        month_code=0
    case '02':
        month_code=3
    case '03':
        month_code=3
    case '04':
        month_code=6
    case '05':
        month_code=1
    case '06':
        month_code=4
    case '07':
        month_code=6
    case '08':
        month_code=2
    case '09':
        month_code=5
    case '10':
        month_code=0
    case '11':
        month_code=3
    case '12':
        month_code=5
    case _:
        print("Inavlid Month Input")

match date_year[0:2]:
    case '17':
        century_code=4
    case '18':
        century_code=2
    case '19':
        century_code=0
    case '20':
        century_code=6

#print("date_year --->",date_year[0:2])

if int(date_year)%4==0:
    if date_month in ['01','02']:
        leap_year_code=1
    else:
        leap_year_code=0
        
day_of_date_input = int((year_code+month_code+century_code+int(date_day)-leap_year_code)%7)

#print(year_code,month_code,century_code,date_day,leap_year_code)

match day_of_date_input:
    case 0:
        date_day_of_week='Sunday'
    case 1:
        date_day_of_week='Monday'
    case 2:
        date_day_of_week='Tuesday'
    case 3:
        date_day_of_week='Wednesday'
    case 4:
        date_day_of_week='Thursday'
    case 5:
        date_day_of_week='Friday'
    case 6:
        date_day_of_week='Saturday'       


#print("Day", date_day)
#print("Month",date_month)
#print("Year",date_year) 
print(date_day,"-",date_month,"-",date_year," is ",date_day_of_week)