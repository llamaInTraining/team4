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

    elif choice == "2":
        print(alert_queue)
        for log in alert_queue:
            print(log)

    elif choice == "3":
        lenght  = len(alert_queue)
        #print(lenght) -- this prints the total number of alarms on the list
        if lenght > 0:
            alarm_resolved = alert_queue.pop(0)
            print("Oldest alert--- ",alarm_resolved," ---has been resolved")
        else:
            print("There are no alarms on the alert queue")
