from locust import HttpUser, task

class ApiLoadTestingUser(HttpUser):
    def on_start(self) :
        response=self.client.post('/accounts/api/v1/jwt/create/',data={"username": "admin","password": "123456"}).json()
        self.client.headers={'Authorization':f"Bearer {response.get('access',None)}"}

    @task
    def task_test(self):
        self.client.get("/api/v1/task/")
