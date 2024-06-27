import os

# Create the days.txt file in the home directory
home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, "days.txt")

with open(file_path, "w") as file:
    # Write the numbers 1 to 30
    for i in range(1, 31):
        file.write(str(i) + "\n")

    # Write the days of the week
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days_of_the_week:
        file.write(day + "\n")