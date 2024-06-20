import os
import time
import random
from datetime import datetime, timedelta
import subprocess

def run_locust(user_count, run_time, report_name):
    """
    Run locust with specified user count and run time.
    """
    locust_path = os.path.join(os.getcwd(), 'env', 'bin', 'locust')
    cmd = [
        locust_path,
        "-f", "load_test.py",
        "--headless",
        "-u", str(user_count),
        "-r", str(user_count // 10),
        "--run-time", run_time,
        "--host", "http://34.45.190.234",  # Update this if necessary
        "--html", report_name
    ]
    subprocess.Popen(cmd).wait()

def generate_load():
    """
    Generate load for 15 minutes with spikes every 2 minutes.
    """
    end_time = datetime.now() + timedelta(minutes=15)
    spike_interval = 2 * 60  # 2 minutes
    spike_duration = 1 * 60  # 1 minute

    report_name = "locust_report.html"

    while datetime.now() < end_time:
        # Normal load
        normal_users = 500
        normal_run_time = "2m"

        print(f"Normal load with {normal_users} users.")
        run_locust(normal_users, normal_run_time, report_name)

        # Spike load
        spike_users = random.randint(2000, 3000)
        spike_run_time = "1m"

        print(f"Spike load with {spike_users} users.")
        run_locust(spike_users, spike_run_time, report_name)

        # Sleep until the next interval
        time.sleep(spike_interval - spike_duration)

if __name__ == "__main__":
    generate_load()
