name = input("Enter your name:  ")
goal = input("Enter one skill you want to get better at: ")
target_month = input("Enter the month you want to reach it by:  ")
daily_minutes = 30

print("\nMy Personal Goal Plan\n")
print("Name: ", name)
print("Goal: ", goal)
print("Target Month: ", target_month)
print("Daily Practice Time: ", daily_minutes, "minutes")
print("Status: ", end=" ")
print("Not Started")
print("Reminder:", end=" - ")
print("Practice Every Day!")
print(name, "plans to work on", goal, "for", daily_minutes, "minutes everyday until", target_month)

