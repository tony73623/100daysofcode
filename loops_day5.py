# fruits=["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+ " Pie")
# average height excercise
student_heights=input("input a list of student heights: ").split()
for n in range (0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

total_height=0
for height in student_heights:
    total_height+=height
print(total_height)

number_of_students=0
for student in student_heights:
    number_of_students+=1

average_height=round(total_height/number_of_students)
print(average_height)
