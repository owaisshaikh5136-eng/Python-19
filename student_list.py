names = ["Asha", "Ravi", "Imran"]
names.append(input("Name to add: "))
remove_name = input("Name to remove (Enter to skip): ")
if remove_name in names:
    names.remove(remove_name)
names.sort()
print(names)
