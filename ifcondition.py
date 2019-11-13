a = input("Enter any number")
a = int(a)
if a<0:
    print("Entered value is negative")
elif a == 0:
    print("Entered value is zero")
elif 0 < a <= 100:
    print("Entered value is between 1 to 100")
else:
    print("Value is above 100")