year = int(input("enter the year:"))
if(year%4==0 or year%100 !=0 and year%400==0):
    print("it is a leap year")
else:
    print("it is not a leap year")