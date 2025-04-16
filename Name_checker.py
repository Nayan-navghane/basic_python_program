# check if the input contains any digit or numbers, or special characters
username = input("what is your name? ")
if(username.isdigit()):
    print("The given input is digit")
elif (username.isalpha()):
    print(username)
else:
    print("The given input is special character")