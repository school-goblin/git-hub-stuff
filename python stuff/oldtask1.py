amount = float(input("how much are you going to invest right now?"))
monthly = float(input("how much are you goint to invest every month"))
rate = float(input("what is your rate? (please put in decimal form. exmple 4.5% would be 4.5)"))
length = float(input("how many years are you going to let it sit"))
length *= 12
rate = rate / 12 / 100


left = amount * (1 + rate) ** length
right = monthly*(((1 + rate) ** length)-1)/rate * (1 + rate)

futuerValue = left + right
print(str(left))
print(str(right))
print(str(futuerValue))
input()