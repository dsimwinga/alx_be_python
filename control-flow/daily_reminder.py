task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task with no time bound, attend to later tomorrow!")
        
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires attention within its time bound!")
        
    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task with time bound. Consider completing it when you have free time tomorrow.")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
            
    case _:
        print("Invalid priority!..")