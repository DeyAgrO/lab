import os
import random
import string

def main():
    user = os.getenv('USER')
    file_path = f"/home/{user}/code.txt"

    with open(file_path, "w") as file:
        for i in range(100):
            if i == 77:  # 78th line (zero-based indexing)
                file.write("ansible-api-token=3092DJA9N9J2198DJ12PUD9AZ82JJE\n")
            else:
                random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(20, 50)))
                file.write(random_text + "\n")

    print(f"Random text file generated: {file_path}")

if __name__ == "__main__":
    main()