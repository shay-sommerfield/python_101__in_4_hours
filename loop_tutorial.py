x = [5,3,8]

# [print(y) for y in x]

# for y in x:
#     print(y)

for i in range(20):
    print(i)



val = 3
# an infinet loop if not for the break statement
# put the cursor in the terminal and press ctrl and c at the same time to stop the program
while True:
    if val <= 0:
        break  # comment this line out to go into an infinite loop
    else:
        print(val)
        val -= 1 # is the same as this: val = val - 1

print("We broke out of the loop")