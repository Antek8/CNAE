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
