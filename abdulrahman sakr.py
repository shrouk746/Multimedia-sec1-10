# Task 1: Budget Affordability Checker
def check_affordability():
    """Check if an item is affordable based on budget and cost."""
    budget = int(input("Enter your total budget: "))
    cost = int(input("Enter the cost of the item: "))
    
    if cost <= budget:
        remainder = budget - cost
        print(f"Success! The item is affordable. You will have ${remainder} remaining.")
    else:
        shortage = cost - budget
        print(f"Alert! You need ${shortage} more to afford this item.")
check_affordability()

# Task 2: Title Case Formatter
def format_title_case():
    """Convert a sentence to Title Case where every word starts with a capital letter."""
    sentence = input("Enter a sentence: ")
    title_case_sentence = sentence.title()
    
    print(f"Original sentence: {sentence}")
    print(f"Title Case sentence: {title_case_sentence}")
format_title_case()

# Task 3: Sum Comparison with 100
def compare_sum_to_100():
    """Calculate sum of two floats and compare against 100."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    total = num1 + num2
    
    if total >= 100:
        print(f"The sum is {total}, which is greater than 100.")
    else:
        print(f"The sum is {total}, which is smaller than 100.")
compare_sum_to_100()    


# Task 4: Remove Item from List
def remove_from_list():
    """Remove an item from a predefined list."""
    my_list = ['Apple', 'Banana', 'Cherry', 'Data']
    
    print(f"Current list: {my_list}")
    item_to_remove = input("Enter the item you want to remove: ")
    
    if item_to_remove in my_list:
        my_list.remove(item_to_remove)
        print(f"Success! '{item_to_remove}' has been removed.")
    else:
        print(f"'{item_to_remove}' was not found in the list.")
    
    print(f"Updated list: {my_list}")
remove_from_list()


# Task 5: Calculate Factorial
def calculate_factorial():
    """Calculate the factorial of a positive integer N."""
    n = int(input("Enter a positive integer N: "))
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    print(f"The factorial of {n} is {result}")
calculate_factorial()
