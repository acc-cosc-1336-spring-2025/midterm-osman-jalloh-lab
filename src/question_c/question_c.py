#write functions here, don't add input('') statements here!
def use_local_variable(num):
    num = 10  # This is a local variable, it won't affect variables outside this function


num = 100
use_local_variable (num)

print("Value of num in the test case:", num)