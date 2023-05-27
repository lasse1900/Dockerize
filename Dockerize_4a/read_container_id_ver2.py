import docker

def copy_file_from_container(container_name, src_path, dest_path):
    client = docker.from_env()
    container = client.containers.get(container_name)

    # Copy the file from the container to a temporary location within the container
    temp_dest_path = "/tmp/temp_file"
    container.exec_run(f"cp {src_path} {temp_dest_path}")

    # Copy the temporary file from the container to the local drive
    container_id = container.id
    copy_command = f"docker cp {container_id}:{temp_dest_path} {dest_path}"
    client.api.exec_create(container_id, copy_command)

# Usage example
# copy_file_from_container("my_container", "/path/to/source/file.txt", "/path/to/destination/file.txt")
copy_file_from_container("26caefee6115", "/app/data.csv", ".")
