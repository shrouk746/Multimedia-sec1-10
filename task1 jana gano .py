def remove_from_list():
    my_list = ['Apple', 'Banana', 'Cherry', 'Data']
    item = input("Enter the item you want to remove: ")
    if item in my_list:
        my_list.remove(item)
        print(f"{item} has been removed successfully!")
    else:
        print(f"{item} was not found in the list.")
    print("Updated list:", my_list)

remove_from_list()