name = input("Enter your name: ") # prompt a user to enter something 

if name.lower() == "shay":  # compare their name to lower case
    print("You are a loser.")
else:
    print("You are probably pretty cool. ")


num = input("Enter a number: ")

if not num.isnumeric():
    raise Exception("You must enter a number") # This is how you raise an error

print("Good Job!")