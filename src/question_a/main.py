import question_a


while True:
    user_input = input("Enter a number to check if it's prime (or type 'quit' to exit): ")
    if user_input.lower() == 'quit':  # Exit condition
        print("Goodbye!")
        break
    try:
        number = int(user_input)  # Convert input to an integer
        result = question_a.is_prime(number)  # Call the is_prime function
        print(f"The number {number} is {'prime' if result else 'not prime'}.")
    except ValueError:
        print("Please enter a valid number or type 'quit' to exit.")

