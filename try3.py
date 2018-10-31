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
