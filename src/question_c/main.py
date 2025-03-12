#add import
# Define the function
def use_local_variable(num):
    num = 10  # Local variable, only exists inside the function

# Main program
if __name__ == "__main__":
    num = 50  # External variable
    print(f"Before calling the function, num = {num}")  # Display the initial value
    use_local_variable(num)  # Call the function
    print(f"After calling the function, num = {num}")  # Display the value after the function call

