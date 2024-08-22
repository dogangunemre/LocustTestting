# Performance Testing the Swagger Petstore API with Locust

In this guide, we will walk through how to perform a performance test on the Swagger Petstore API using Locust. Locust is a user-friendly, Python-based load testing tool that allows you to define user behavior and simulate thousands of concurrent users accessing your application.

## Prerequisites

Before starting, ensure you have the following installed:

- **Python**: Locust is a Python-based tool, so you need Python installed on your system.
- **pip**: Python package installer, used to install Locust.
- **Locust**: You can install it using pip.

    ```bash
    pip install locust
    ```

## Setting Up the Locust Test

Create a file named `locustfile.py` in your project directory. This file will define the behavior of the virtual users.

Here is an example of what your `locustfile.py` could look like:

```python
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
