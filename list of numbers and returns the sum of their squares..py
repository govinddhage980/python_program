def sum(numbers):
    total = 0
    for num in numbers:
        total = total + num ** 2 # 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30
    return total


print(sum([1, 2, 3, 4]))





#without function
numbers = [1, 2, 3, 4]
total = 0

for num in numbers:
    total = total + num ** 2 ## 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30


print("Sum of squares:", total)
