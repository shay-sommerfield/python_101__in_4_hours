x = [1, 3,"thing"] # list of values set in an order
#    0, 1,   2   are the corresponding indices

print(f"The val in the 0th position of x: {x[0]}")
print(f"The length of x: {len(x)}.")

# these are all thse same for the for loop
index_values = [0,1,2]
index_values = range(3)
index_values = range(len(x))

for index in index_values:
    print(x[index_values])

# for index in range(len(x)):
#     print(x[index])

# for thing in x:
#     print(thing)