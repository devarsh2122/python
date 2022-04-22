# A list containing redundant data
a = [1, 3, 4, 1, 2, 2, 5, 2, 1, 7, 0, 9]
#Take an Empty List
c = []
# Traverse the list a using for loop
# Add the element to the list c if it does not exist
for i in a:
    if i not in c:
        c.append(i)
# Printing the result
print(c)

