def calculate_factorial():
    N = int(input("Enter a positive integer: "))
    result = 1
    for i in range(1, N + 1):
        result *= i
    print("The factorial of", N, "is:", result)

calculate_factorial()