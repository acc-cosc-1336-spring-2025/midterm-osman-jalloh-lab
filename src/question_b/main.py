#add import
from question_b import reverse_string
while True:
    user_input=input("enter a word or quit to stop: ")
    if user_input=="quit":
        break
    print(reverse_string(user_input))    