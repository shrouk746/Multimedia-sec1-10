def remove_from_list():
    my_list = ['Apple', 'Banana', 'Cherry', 'Data']
    
    print("Current List: " + str(my_list))

    item_to_remove = input("Enter the item you want to remove: ")

    if item_to_remove in my_list:
        my_list.remove(item_to_remove)
        
        print("SUCCESS: '" + item_to_remove + "' has been removed.")
    else:
        
        print("ERROR: '" + item_to_remove + "' was not found in the list.")

    
    print("Final Updated List: " + str(my_list))

remove_from_list()