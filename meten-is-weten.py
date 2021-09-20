a = input("Geef getal 1 op= ")
b = input("geef getal 2 op= ")

if a > b:
    max = a
    min = b
    print("a is het grootste getal")
elif a < b:
    min = a
    max = b
    print("a is het kleinste getal")
else: #ik kon hier niet a == b gebruiken want dat gaf een syntax error
    min = a
    max = b
    print("a en b zijn even groot")

print("het minimum is: " + str(min))
print("het maximum is: " + str(max))