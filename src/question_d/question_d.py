#write functions here, don't add input('') statements here!
# Function to calculate assessment value
def get_assessment_value(value):
    return value * 0.6  # Assessment value is 60% of the actual value

# Function to calculate property tax
def get_tax_assessed(assessment_value):
    return (assessment_value / 100) * 0.72  # Tax is 72¢ per $100 of assessment value

# Main program
