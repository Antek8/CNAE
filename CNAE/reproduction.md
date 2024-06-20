# Reproduction Guide: Load Generation for Microservices Architecture

This guide will walk you through the steps to reproduce the load generation setup and test the performance of your microservices architecture using Locust. The steps include setting up the environment, creating the necessary scripts, and running the load tests.

## Prerequisites

1. **Google Cloud Project**: Ensure you have a Google Cloud project created.
2. **Google Cloud SDK**: Ensure you have the Google Cloud SDK installed and initialized.
3. **Kubernetes Cluster**: Ensure you have a Kubernetes cluster running on Google Kubernetes Engine (GKE).
4. **Locust**: Ensure Locust is installed.

## Step-by-Step Instructions

1. **Clone the Microservices Demo Repository**

    ```sh
    git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
    cd microservices-demo
    ```

2. **Set Up the Environment**

    Create and activate a Python virtual environment:

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Locust**

    ```sh
    pip install locust
    ```

4. **Create the Load Test Script**

    Create a file named `load_test.py` with the following content:

    ```python
    from locust import HttpUser, TaskSet, task, between

    class UserBehavior(TaskSet):
        @task(1)
        def ad_service(self):
            self.client.get("/ads")

        @task(2)
        def cart_service(self):
            self.client.get("/cart")

        @task(3)
        def checkout_service(self):
            self.client.get("/checkout")

        @task(4)
        def currency_service(self):
            self.client.get("/currency")

        @task(5)
        def email_service(self):
            self.client.get("/email")

        @task(6)
        def product_catalog_service(self):
            self.client.get("/products")

        @task(7)
        def recommendation_service(self):
            self.client.get("/recommendations")

        @task(8)
        def shipping_service(self):
            self.client.get("/shipping")

        @task(9)
        def frontend(self):
            self.client.get("/")
    
    class WebsiteUser(HttpUser):
        tasks = [UserBehavior]
        wait_time = between(1, 5)  # Simulate users waiting between 1 and 5 seconds between tasks
    ```

5. **Create the Load Generation Script**

    Create a file named `generate_load.py` with the following content:

    ```python
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

            # Spike load. The app will crash above 2000 users
            spike_users = random.randint(2000, 3000)
            spike_run_time = "1m"

            print(f"Spike load with {spike_users} users.")
            run_locust(spike_users, spike_run_time, report_name)

            # Sleep until the next interval
            time.sleep(spike_interval - spike_duration)

    if __name__ == "__main__":
        generate_load()
    ```

6. **Deploy and Run the Load Generation Script**

    - **Use `tmux` or `screen` to run the script in a persistent session**:

        ```sh
        tmux new -s load-generator
        ```

        Within the `tmux` session:

        ```sh
        source env/bin/activate
        python3 generate_load.py
        ```

        Detach from the `tmux` session by pressing `Ctrl+B`, then `D`.

    - **To reattach to the `tmux` session later**:

        ```sh
        tmux attach -t load-generator
        ```

7. **Verify and Retrieve the Report**

    After the 15-minute load test completes, a report will be generated in the file `locust_report.html`.

    - **Transfer the report to your local machine**:

        ```sh
        gcloud compute scp [YOUR_INSTANCE_NAME]:~/locust_report.html .
        ```

        Replace `[YOUR_INSTANCE_NAME]` with the name of your Compute Engine instance.

8. **Analyze the Report**

    Open `locust_report.html` in a web browser to view detailed metrics, including request latency, error rates, and response times.

## Conclusion

By following these steps, you can reproduce the load generation setup and test the performance of your microservices architecture using Locust. The generated report will provide valuable insights into the system's scalability, reliability, and performance under load.
