name = input("Enter five names: ")
name_list = name.lower().split()
for name in name_list:
    name_list.sort()
    print(f"{name}\n")