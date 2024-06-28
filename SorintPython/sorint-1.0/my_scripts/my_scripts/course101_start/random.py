import os
import random
import string

def main():
    # Get the current user's home directory
    user = os.getenv('USER')
    random_dir = f"/home/{user}/random"

    # Create the 'random' directory if it doesn't exist
    if not os.path.exists(random_dir):
        os.makedirs(random_dir)
        print(f"\033[92mThe '{random_dir}' directory has been created.\033[0m")
    else:
        print(f"\033[92mThe '{random_dir}' directory already exists.\033[0m")

    # Generate 10 .mp3 files
    for i in range(10):
        file_name = f"random_{i}.mp3"
        file_path = os.path.join(random_dir, file_name)
        with open(file_path, "w") as file:
            file.write("This is a random .mp3 file.")

    # Generate 6 .mp4 files
    for i in range(6):
        file_name = f"random_{i}.mp4"
        file_path = os.path.join(random_dir, file_name)
        with open(file_path, "w") as file:
            file.write("This is a random .mp4 file.")

    # Generate 8 .jpg files
    for i in range(8):
        file_name = f"random_{i}.jpg"
        file_path = os.path.join(random_dir, file_name)
        with open(file_path, "w") as file:
            file.write("This is a random .jpg file.")

    # Generate 5 .wav files
    for i in range(5):
        file_name = f"random_{i}.wav"
        file_path = os.path.join(random_dir, file_name)
        with open(file_path, "w") as file:
            file.write("This is a random .wav file.")

if __name__ == "__main__":
    create_random_files()