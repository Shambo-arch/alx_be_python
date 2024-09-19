task = input("Enter your task: ")
priority = input("Enter its priority (high, medium, low): ")
time_bound = input("Is it time-bound (yes or no): ")
match priority:
    case "high":
        if time_bound == "yes" or "no":
            print(f"Reminder: {task} is a high priority that requires immediate attetion today!")
    case "medium":
        if time_bound == "yes" or "no":
            print(f"Okey, {task} is a medium priority that must be planned accordingly!")
    case "low":
        if time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"If {task} is time-bound, it is okey for you!")

        
