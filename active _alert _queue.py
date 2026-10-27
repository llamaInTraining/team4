#active alert queue 
alert_queue = []
while True:
    #add menu list
    print("---Security Operation Center Main menu---")
    print("Option 1. New Log Alert ")
    print("Option 2. View Active Queue ")
    print("Option 3. Resolve Oldest Alert")
    print("Option 4.  Exit System")
    choice = input("Please choose from the menu: ")
    if choice == "1":
     #This choie allows user to log new alert
        alert = input(" please enter the alert--- ")
        alert_queue.append(alert)
        print("Alert logged successfully!")
        break