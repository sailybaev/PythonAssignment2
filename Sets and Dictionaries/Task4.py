pairs = [(input("Enter key: "), input("Enter value: ")) for _ in range(3)]
user_dict = dict(pairs)

key_to_check = input()
if key_to_check in user_dict:
    print(f"{key_to_check} exists in the dictionary with value: {user_dict[key_to_check]}")
else:
    print(f"{key_to_check} doesn't exist in the dictionary.")
