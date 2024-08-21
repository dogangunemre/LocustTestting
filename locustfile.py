from locust import HttpUser, task, between


class PetstoreUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_pets(self):
        self.client.get("/v2/pet/findByStatus?status=available")

    @task
    def get_pet_by_id(self):
        pet_id = 1  # Example pet ID
        self.client.get(f"/v2/pet/{pet_id}")

    @task
    def add_pet(self):
        pet_data = {
            "id": 0,
            "category": {"id": 0, "name": "string"},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
        self.client.post("/v2/pet", json=pet_data)
