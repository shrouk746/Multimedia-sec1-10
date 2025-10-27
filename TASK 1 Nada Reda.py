def remove_from_list():
    my_list = ['Apple', 'Banana','Cherry', 'Data']
    item_want_to_remove =  input("Enter the item you want to remove:")
    if item_want_to_remove in my_list:
        my_list.remove(item_want_to_remove)
        print("success: " + item_want_to_remove+" has been removed.")
    else:
        print("error :"+item_want_to_remove+" was not found in the list .")
        print("final update :"+ str(my_list))

remove_from_list()
    