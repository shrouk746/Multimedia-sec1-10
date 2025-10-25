def calculate_factorial():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Please enter a positive integer.")
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("The factorial of", n, "is", result)

calculate_factorial()