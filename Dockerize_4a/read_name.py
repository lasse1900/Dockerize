import docker

def get_container_name(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    return container.name

# Usage example
# container_id = "your_container_id"
container_id = "26caefee6115"
container_name = get_container_name(container_id)
print(container_name)
