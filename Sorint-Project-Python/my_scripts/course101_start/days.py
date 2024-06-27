import os

def main():
    # Create the days.txt file in the home directory
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, "days.txt")

    if os.path.exists(file_path):
        print(f"\033[92mThe 'days.txt' file already exists in the home directory: {home_dir}\033[0m")
    else:
        with open(file_path, "w") as file:
            # Write the numbers 1 to 30
            for i in range(1, 31):
                file.write(str(i) + "\n")

            # Write the days of the week
            days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            for day in days_of_the_week:
                file.write(day + "\n")

        print(f"\033[92mThe 'days.txt' file has been created in the home directory: {home_dir}\033[0m")

if __name__ == "__main__":
    main()