Adam Mohamed, Rached Aissa, Joseph Sanchez, Omer Faruk
 #Immutable Inventory Tracker
#Team work on the IT Procurement and Deployment department that is going to trac a company's dynamic stocks of laptops.
#1st we will creat a list of approved device models that are allowed to be used in the company. This list will be immutable, meaning it cann't be changed or modified.
#then we will creat a mutable list that will be used to track the current inventory of devices in the company. This list can be modified by adding or removing item as needed.
#After that will creat a simple user interface that will allow the user to add, remove, and view the current inventory of devices in the company. The user will be prompted to enter their choice, and the program will respond accordingly.
#Then we will implement a check to ensure that only approved device models can be added to the inventory. If the device model is not listed, the program will display an error message and not add the item on the inventory list
#Then we will implement a check to ensure that only items that are already in the inventory can be removed. If the item is not found, the program will display an eror message and not remove the item from the inventory list.
#Then we will implement a view option that will display the current inventory of devices in the company. The user will be able to see the list of devices that are currently added to the inventory.
#Then we will implement an exit option that will allow the user to exit the program. When the user chooses to exit, the program will display a thank you message and terminated.
 
 
approved_models = ("MacBook Pro", "Dell XPS", "ThinkPad" "HP Spectre", "Surface Laptop", "Asus ZenBook")
 
# Mutable inventory list
device_inventory = []
 
while True:
    print("\n1: Add")
    print("2: Remove")
    print("3: View")
    print("4: Exit")
 
    choice = input("Enter choice: ")
 
    if choice == "1":
        print("Approved device models:", approved_models)
        new_item = input("Enter the new item: ")
 
        if new_item in approved_models:
            device_inventory.append(new_item)
        else:
            print("Error: Device model not approved for company use.")
 
    elif choice == "2":
        print(device_inventory)
        delete = input("Enter item to remove: ")
 
        if delete in device_inventory:
            device_inventory.remove(delete)
        else:
            print("Device not found.")
 
    elif choice == "3":
        print(device_inventory)
 
    elif choice == "4":
        print("Thank you for using our system.")
        break
 
    else:
        print("Invalid choice.")
 
