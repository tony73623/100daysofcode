print("Welcome to the rollercoster!")
height=int(input("what is your height in cm?: "))
age=int(input("enter the age:"))
bill=0
if height>=120:

    if (age<12):
        bill=5
        print("tickets for children are $5")
    elif (age<=18):
        bill=7
        print("tickets for youth is $7")
    elif (age>18):
        bill=12
        print("adult tickets are $12")

    wants_photo=input("Do you want a photo taken? Y or N: ")
    if wants_photo=="Y":
        bill=bill+3

    print(f"your final bill is {bill}")
else:
    print("sorry you need to grow taller")
