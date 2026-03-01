def check_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

number = int(input("Enter a Number: "))
result = check_prime(number)
print("The number is:", result)
