mark = [96,54,76,56]

mark.append(50) #It new add element in the list
print(mark)

mark.pop() # it delete the element in the list
print(mark)




# . Create a dic onary represen ng a student with keys for "name," "age," and "grade." Print each key-value pair.



student = {
    "name": "Govind",
    "age": 20,
    "grade": "A",
    "mark": 34
}

print(student)

for key, value in student.items():
    print(f"{key}: {value}")



#Write a program that checks if a given number is greater than 10 and prints

number = int(input("Enter the number: "))

if number > 10:
    print("The number is greater than 10.")
else:
    print("The number is not greater than 10.")


#useig function
def check_number(num):
    if num > 10:
        print("number is greater than 10.")
    else:
        print("number is not greater than 10.")
check_number(6)