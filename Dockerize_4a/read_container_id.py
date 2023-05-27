import docker

# Create a Docker client
client = docker.from_env()

# Get a list of running containers
containers = client.containers.list()
print(f"containers: {containers} ")
print("Trying to read Docker container ID")

try:
    # Iterate over the containers and print their IDs
    for container in containers:
        print("Container ID:", container.id)

    containerID = container.id
    print(f"containerID name: {containerID}")
    cut_containerID = containerID[:12].ljust(12)
    print(f"shortened Container ID: {cut_containerID}")
except:
    print("No containers running currently")

