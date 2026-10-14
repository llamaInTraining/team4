Adam Mohamed, Rached Aissa, Joseph Sanchez, Omer Faruk 
#Create a program that approves only approved products
#Aprroved products Macbook Pro, Dell XPS, ThinkPad
#Tuples: Create approved_models with at least three approved devices using parentheses ().
#Initialize an empty device_inventory list
#Create a while True: menu with options 1 (Add), 2 (Remove), 3 (View), and 4 (Exit).
#Prompt for a device, validate it against approved_models, and use if approved.
#Print device_inventory when option 3 is selected.
#Check if item in device_inventory: before using .remove(); otherwise, print "Device not found.".
#Use break when option 4 is selected.
#Display an error message for unapproved devices and invalid menu choices.
approve_models = ["MacBook Pro", "Dell XPS", "ThinkPad"]
device_inventory= []
while True:
    print("1: Add: ")
    print("2: remove: ")
    print("3: View: ")
    print("4: Exit: ")
    choice = input("enter choice: ")
    if choice == "1":
        new_item = input("enter the new item:  ")
        if new_item in approve_models:
            device_inventory.append(new_item)
        else:
            print("device not approved")
    elif choice == "2":
        print(device_inventory)
        delete = input("enter item to remove:  ")
        if delete in approve_models:
            device_inventory.remove(delete)
        else:
            print("device not on the list")
    elif choice == "3":
        print(device_inventory)
    elif choice == "4":
        print("thank you for using our system ")
        break
    else:
        print("not available. ")
