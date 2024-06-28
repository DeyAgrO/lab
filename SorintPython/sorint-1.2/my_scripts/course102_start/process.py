import subprocess

def start_sleep_processes(count, duration):
    for _ in range(count):
        subprocess.Popen(['sleep', str(duration)])

def main():
    # Number of sleep processes to start
    process_count = 3
    # Duration in seconds (24 hours)
    sleep_duration = 24 * 60 * 60
    
    start_sleep_processes(process_count, sleep_duration)
    print(f"Started {process_count} sleep processes each for {sleep_duration} seconds.")

if __name__ == "__main__":
    main()
