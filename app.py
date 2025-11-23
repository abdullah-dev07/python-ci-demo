def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

def welcome_message():
    """Returns a simple greeting."""
    return "Hello from the CI Pipeline!"

if __name__ == '__main__':
    # This runs if the script is executed directly
    print(welcome_message())
    print(f"The sum of 5 and 7 is: {calculate_sum(5, 7)}")