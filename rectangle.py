import calculate

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
def new_func(perimeter):
    print(f"The perimeter of the rectangle is: {perimeter}")

new_func(perimeter)
