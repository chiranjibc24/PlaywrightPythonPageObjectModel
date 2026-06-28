from locust import HttpUser, between

class DummyJsonUser(HttpUser):
    host = "https://dummyjson.com"
    wait_time = between(1, 5)

    @task
    def get_products(self):
        self.client.get