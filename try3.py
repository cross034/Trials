x = [1, 2, 3]
y = x
x.append(4)     # Mutation
print(y)        # [1, 2, 3, 4]
x = x + [5]     # Rebinding
print(y)        # [1, 2, 3, 4]
print(x)        # [1, 2, 3, 4, 5]

z = x
x += [6]        # Mutation, __iadd__(self, other) is called which extends list with other
print(z)        # [1, 2, 3, 4, 5, 6]

# ----------------------------------------------------------------------------------------

list1 = [1, 2, 3]
def append_list_works(some_list):     # Mutation - works
    some_list.append(100)

def append_list_useless(some_list):   # Rebinding - useless
    some_list = some_list + [100]

def append_list_good(some_list):      # Rebinding, return list - prefarable
    some_list = some_list + [100]
    return some_list

append_list_works(list1)
print(list1)        # [1, 2, 3, 100]
append_list_useless(list1)
print(list1)        # [1, 2, 3, 100]
list1 = append_list_good(list1)
print(list1)        # [1, 2, 3, 100, 100]

# ----------------------------------------------------------------------------------------

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in mat:
    row += [10] # [[1, 2, 3, 10], [4, 5, 6, 10], [7, 8, 9, 10]] - mutation
print(mat)

arr = [1, 2, 3]
for num in arr:
    num += 10
print(arr)      # [1, 2, 3] - rebinding
