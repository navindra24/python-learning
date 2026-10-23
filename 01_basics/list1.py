
num = int(input("Enter a num: "))
if num > 0:
    print("positve")
elif num < 0 :
    print("negative")
elif num == 0:
    print("zero")

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)



num1 = int(input("enter a num: "))
if num1%3 == 0 and num1%5 == 0:
    print("yup both")
elif num1%3 == 0:
    print("only 3")
elif num1% 5 == 0:
    print("only 5")
else:
    print("not divisble")

units = int(input("enter units consumed: "))
if units >= 0 and units<= 100:
    bill = units * 2
    print("$",bill)
elif units >= 101 and units<= 200:
    bill = units * 3
    print(bill)
elif units >= 201 and units<= 300:
    bill = units * 5
    print(bill)
elif units>300:
    bill = units * 7
    print(bill)

    
