import random
names_string=input("give me everybody's names, seperated by comma: ")
names=names_string.split(",")
print(names)
length_of_names=len(names)
print(length_of_names)
bill_payer=random.randint(0,length_of_names-1)
name_of_payer=names[bill_payer]
print(f"today {name_of_payer}, going to buy food")
