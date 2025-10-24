def calculate_factorial():
    n = int(input("Enter a positive integer: "))
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Factorial =", result)

calculate_factorial()
