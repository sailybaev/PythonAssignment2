pairs = [(input("Enter key: "), input("Enter value: ")) for _ in range(3)]
user_dict = dict(pairs)

values = user_dict.values()
print("Values in the dictionary:", list(values))
