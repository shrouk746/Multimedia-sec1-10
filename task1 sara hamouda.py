def remove_from_list():
    my_list = ['Apple', 'Banana', 'Cherry', 'Data']
    print(f"Current List: {my_list}")

    item_to_remove = input("Enter the item you want to remove: ").strip()

    if item_to_remove in my_list:
        my_list.remove(item_to_remove)
        print(f"'{item_to_remove}' was successfully removed.")
    else:
        print(f"Error: Item '{item_to_remove}' was not found in the list.")

    print(f"Final List: {my_list}")

remove_from_list()