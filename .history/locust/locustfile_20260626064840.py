from locust import HttpUser, task, between

class DummyJsonUser(HttpUser):
    host = "https://dummyjson.com"
    wait_time = between(1, 2)

    @task
    def get_products(self):
        self.client.get("/products")

    @task
    def get_users(self):
        self.client.get("/users")