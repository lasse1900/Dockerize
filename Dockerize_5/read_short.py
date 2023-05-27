import docker
import subprocess

src_path = "/app/data.csv"
dest_path = "."

def get_container_id():
    client = docker.from_env()
    containers = client.containers.list()

    try:
        for container in containers:
            containerID = container.id
        cut_containerID = containerID[:12].ljust(12)
        print(f"shortened Container ID: {cut_containerID}")
    except:
        print("No containers running currently")
    return(cut_containerID)

cutId = get_container_id()

def docker_cp(container_id, src_path, dest_path):
    command = f"docker cp {container_id}:{src_path} {dest_path}"
    subprocess.run(command, shell=True)

docker_cp(cutId, src_path, dest_path)

