# empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert 15 at second position
my_list.insert(1,15)

# extend list
my_list1 = [50, 60, 70]
my_list.extend(my_list1)

# Remove the last element from my_list.
my_list = my_list[:-1]

# sort
my_list.sort()

# index of element 30
indx = my_list.index(30)
print(indx)