# def greet():
#     print("Hello")
#     print("Hi")
#     print("How are ye!")
#
# greet()
#
# #Function that allows for input
# def greet_with_name(name):
#     print(f"hello! how are ya?{name}")
# greet_with_name("Malleswararao")

#Functions wit more than 1 input
def greet_with(name,location):
    print(f"your name is{name}")
    print(f"your location is {location}")
greet_with(" Malleswara rao","chilakaluripet")

#functions with key word arguments
def greet_with_keyword_arg(location="london",name="Angela"):
    print(f"hello {name}")
    print(f"you are from {location}")
greet_with_keyword_arg()


