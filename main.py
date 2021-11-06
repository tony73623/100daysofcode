# two_digit_number=input("enter a two digit number:")
# first_digit=int(two_digit_number[0])
# second_digit=int(two_digit_number[1])
# print(first_digit+second_digit)

# num=int(input("enter a number:"))
# result=0
# hold=num
#
# while num>0:
#     rem=num % 10
#     result=result+num
#     num=int(num/10)
#
# print("sum of all digits of",hold,"is: ",result)

num = int(input("Enter a Number: "))
result = 0
hold = num

# while loop to iterate through all the digits of input number
while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)

# displaying output
print("Sum of all digits of", hold, "is: ", result)

