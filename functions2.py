import math

test_h=float(input("Height of wall: "))
test_w=float(input("width of wall: "))
coverage=5
def paint_calc(height=test_h, width=test_w,cover=coverage):
    number_of_cans=(height*width)/coverage
    print(math.ceil(number_of_cans))
    print(round(number_of_cans))
paint_calc()