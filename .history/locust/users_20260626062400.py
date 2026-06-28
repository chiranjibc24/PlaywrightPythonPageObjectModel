from locust import HttpUser

class DummyJsonUser(HttpUser):
    host = "https://dummyjson.com"
    wait_time = between