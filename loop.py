import os
import signal
import time
import subprocess


# Join :- @Sainiddos # Set the path to the script you want to restart
script_to_restart = "new.py"

def restart_script():
    # Join :- @Sainiddos # Run the script
    print("chal raha hai bc.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(480)  # Join :- @Sainiddos # Sleep for 30 seconds
        # Join :- @Sainiddos # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # Join :- @Sainiddos # Wait for the process to terminate
        process.wait()
        # Join :- @Sainiddos # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()