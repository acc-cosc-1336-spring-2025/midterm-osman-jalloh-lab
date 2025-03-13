#add import

from question_d import get_assessment_value, get_tax_assessed  # Replace with your actual filename

if __name__ == "__main__":
    while True:
        try:
            # Prompt user for actual property value
            user_input = input("Enter the actual value of the property (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                print("Exiting program. Goodbye!")
                break
            
            actual_value = float(user_input)  # Convert to float
            # Calculate assessment value and property tax
            assessment_value = get_assessment_value(actual_value)
            tax = get_tax_assessed(assessment_value)
            
            # Display results
            print(f"Assessment Value: ${assessment_value:.2f}")
            print(f"Property Tax: ${tax:.2f}")
        
        except ValueError:
            print("Invalid input. Please enter a valid number for the property value.")
