import docker
import subprocess

src_path = "/app/data.csv"
dest_path = "."

def get_container_id():
    # Create a Docker client
    client = docker.from_env()

    # Get a list of running containers
    containers = client.containers.list()
    # print(f"containers: {containers} ")

    try:
        # Iterate over the containers and print their IDs
        for container in containers:
            # print("Container ID:", container.id)
            containerID = container.id
        # print(f"containerID name: {containerID}")
        cut_containerID = containerID[:12].ljust(12)
        print(f"shortened Container ID: {cut_containerID}")
    except:
        print("No containers running currently")
    return(cut_containerID)

id = get_container_id()

def get_container_name(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    return container.name

def docker_cp(container_id, src_path, dest_path):
    command = f"docker cp {container_id}:{src_path} {dest_path}"
    subprocess.run(command, shell=True)

# Usage example
container_id = id
container_name = get_container_name(container_id)
print(container_name)

docker_cp(container_id, src_path, dest_path)