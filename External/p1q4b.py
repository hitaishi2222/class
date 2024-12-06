# calculate area of rectangle
def area_rectangle(length: float, breadth:float):
    print(f"Area of given rectangle is {length * breadth}.")
    return length * breadth


# find the maximum of list of numbers
def maximum(list: list):
    print(f"The maximum number in the given list is {max(list)}")

# greeting user
greet = "Welcome "
def greet_user(name: "str"):
    print(greet + name + "...")

area_rectangle(2,4)

a = [24,12,3,45,987,321,989,31,68]
maximum(a)

greet_user("Hema")
