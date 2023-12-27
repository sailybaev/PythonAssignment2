pairs = [(input("Enter key: "), input("Enter value: ")) for _ in range(3)]
user_dict = dict(pairs)

key_to_remove = input("Enter the key to remove: ")
if key_to_remove in user_dict:
    del user_dict[key_to_remove]
    print(f"{key_to_remove} removed from the dictionary.")
else:
    print(f"{key_to_remove} not found in the dictionary.")
