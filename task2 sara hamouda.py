def calculate_factorial():
    while True:
        try:
            # Prompt the user to enter a positive integer N
            N = int(input("Enter a positive integer (N) to calculate its factorial: "))
            if N >= 0:
                break
            else:
                print("Please enter a positive integer (N >= 0).")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Initialize a variable named result to 1 (0!=1)
    result = 1

    # Use a for loop along with the range() function to iterate from 1 up to N
    for i in range(1, N + 1):
        # Inside the loop, multiply the current number by the current result
        result = result * i

    # Print the final factorial value
    print(f"The factorial of {N} is: {result}")

calculate_factorial()