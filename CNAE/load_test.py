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
