# create an empty list
my_list=[]

# Append elements 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15
my_list.insert(1, 15)

# Extend the list
my_list.extend([50,60,70])

# Remove the last element
my_list.pop()

# Find and print the index of the value 30
index_of_30= my_list.index(30)

print("Final list:", my_list)
print("Index of 30:", index_of_30)