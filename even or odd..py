# using function
def even_odd(num):
    if num % 2 == 0:
        print("is Even", num)
    else:
        print("is Odd",num)


even_odd(6)



def even_odd_using_while(limit):
    num = 2
    while num <= limit:
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")
        num += 2

even_odd_using_while(10)



#without fuction

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("number is Even", number)
else:
    print("number is Odd", number)
