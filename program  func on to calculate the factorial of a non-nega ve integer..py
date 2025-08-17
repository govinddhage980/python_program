num = int(input("Enter a non-negative numer"))

if num < 0:
    print("Factorial is not defined for negative numbers") #If the number entered by the user is less than 0 (e.g., -1, -5), then factorial cannot be calculated
else:
    result = 1
    for i in range(1, num + 1):
        result = result * i      #result*=1
    print(f"Factorial of is ", result)


#using function

def faC(num):
    if num < 0:
        print("Factorial is not defined for negative numbers")
    else:
        result = 1
        for i in range(1, num + 1):
            result = result * i
        print("Factorial of is :",  result)

faC(3)