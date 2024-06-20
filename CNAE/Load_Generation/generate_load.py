import os
import time
from datetime import datetime, timedelta
import subprocess
import random  # Add this import

def run_locust(user_count, run_time):
    """
    Run locust with specified user count and run time.
    """
    cmd = [
        "locust",
        "-f", "load_test.py",
        "--headless",
        "-u", str(user_count),
        "-r", str(user_count // 10),
        "--run-time", run_time,
        "--host", "http://34.45.190.234"  # Replace with your frontend-external LoadBalancer IP
    ]
    subprocess.Popen(cmd).wait()

def generate_load():
    """
    Generate load with random spikes for 24 hours.
    """
    end_time = datetime.now() + timedelta(hours=24)
    while datetime.now() < end_time:
        # Base load
        user_count = random.randint(10, 50)
        run_time = "1h"

        # Random spike
        if random.random() < 0.3:  # 30% chance of a spike
            spike_users = random.randint(200, 1000)
            print(f"Spike! Adding {spike_users} users.")
            run_locust(spike_users, "10m")  # Run the spike for 10 minutes

        # Normal load
        print(f"Normal load with {user_count} users.")
        run_locust(user_count, run_time)

        # Sleep for the remainder of the hour
        sleep_time = 3600 - (datetime.now().minute * 60 + datetime.now().second)
        print(f"Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)

if __name__ == "__main__":
    generate_load()
