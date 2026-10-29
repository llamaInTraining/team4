#Adam Mohamed, Rached Aissa, Joseph Sanchez, Omer Faruk
#active alert queue 
#goalis to build an interactive, dynamic "Active Alert Queue" that logs, views, and resolve incoming threats.
#Initialize an empty list named alert_queue and use a while True loop to continuously serve a main menu
#Prompt the user for a threat description using input()
# use .append() to place the alert at the end of the queue, and display "Alert logged successfully!"
#Display all pending alerts under the heading "--- Current Pending Alerts ---"
#Keep track of unresolved threats so the analyst knows which issues still need attention.
#Make it easier to review multiple alerts in one place and prioritize which threats need to be addressed.
#Prevent unnecessary errors when there are no pending alerts to display.
#Improve organization by keeping all active alerts visible until they are resolved.
#Resolve the oldest pending alert first to ensure threats are handled in the order they were received.
#Remove resolved alerts from the queue to keep the list updated and organized.
#Confirm when an alert has been resolved so the analyst knows it has been cleared.
#Check whether alerts exist before removing one to prevent errors when the queue is empty.
#Notify the analyst when there are no pending alerts left to resolve.
#Maintain an organized workflow so unresolved threats are not overlooked.
#Option to exit System: Break the loop and terminate the program.
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

    elif choice == "4":
        print("Exit the system")
        break

    else:
        print("please choose between choices 1-4")
