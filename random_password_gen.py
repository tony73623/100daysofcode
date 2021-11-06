#password generator project
def password_gen():
    import random
    alphabets=['a','b','b','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','%','^','&','*','(',')']

    print("Welcome to the PyPassword Generator!")
    input_letters=int(input("Enter the number of letters you want in your password: "))
    input_symbols=int(input("How many symbols would like: "))
    input_numbers=int(input("How many numbers would you like:"))

    # easy level
    # password=""
    #
    # for alphabet in range (1, input_letters+1):
    #     password+=random.choice(alphabets)
    # for alphabet in range (1, input_symbols+1):
    #     password+=random.choice(symbols)
    # for alphabet in range (1, input_numbers+1):
    #     password+=random.choice(numbers)
    # print(password)

    #hard level

    password_list=[]

    for alphabet in range (1, input_letters+1):
        password_list.append(random.choice(alphabets))
    for number in range (1, input_symbols+1):
        password_list+=random.choice(symbols)
    for symbol in range (1, input_numbers+1):
        password_list+=random.choice(numbers)
    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password=""
    for char in password_list:
        password+=char
    print(f"your password is :{password} ")

print(password_gen())