my_set = {1, 2, 3, 4, 5}
element_to_check = int(input("Enter an element to check in the set: "))

if element_to_check in my_set:
    print(f"{element_to_check} is present in the set.")
else:
    print(f"{element_to_check} is not present in the set.")
