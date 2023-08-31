#Assignment 1
#Spencer Smith

def part1():
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))

    BMI = (weight * 703) / (height)**2
    print(BMI)

    if (BMI < 18.5):
        print("You are underweight.")
    elif (BMI > 25):
        print("You are overweight.")
    else:
        print("You are an ideal weight.")
part1()

def part2():
    sum = 0
    for x in range(2, 101, 2):
        sum += x
    print("The sum of even numbers from 2 to 100 is:", sum)
part2()

def part3():
    a = int(input("Enter the starting number: "))
    b = int(input("Enter the ending number: "))
    sum2 = 0
    for y in range(a, b + 1):
        if y % 2 != 0:
            sum2 += y
    print("The sum of even numbers from", a, "to", b, "is:", sum2)
part3()

def part4():
    targetPrice = float(input("Enter the target price: "))
    currentPrice = 0.0
    while currentPrice < targetPrice:
        currentPrice = float(input("Enter the current price: "))
    print("The shares can be sold now.")
part4()

def part5():
    tuition = 8000
    for z in range(1, 6):
        tuition *= 1.03
        print("The tuition for year", z, "is", round(tuition, 2))
part5()