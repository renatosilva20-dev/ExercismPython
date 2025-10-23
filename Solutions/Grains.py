total = 0 
grains = 1
def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    elif number>=1 or number <=64:
        number = 2**(number-1)
    return number
def total():
    return 2**64 - 1