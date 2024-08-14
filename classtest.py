class Foo:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

door = Foo(size='180x70', color='red chestnut', material='oak')
print(door.size) #180x70






# Example list of strings
string_list = ['a', 'b', 'c']

# Create global variables with names based on the list items
for v in string_list:
    globals()[f'{v}'] = 0

# Print the values of the created variables
print(a)
print(b)
print(c)