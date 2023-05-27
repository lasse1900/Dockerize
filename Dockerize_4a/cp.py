import subprocess

def docker_cp(container_id, src_path, dest_path):
    command = f"docker cp {container_id}:{src_path} {dest_path}"
    subprocess.run(command, shell=True)

# Usage example
# container_id = "your_container_id"
# src_path = "/path/to/source/file.txt"
# dest_path = "/path/on/local/drive/file.txt"
container_id = "26caefee6115"
src_path = "/app/data.csv"
dest_path = "."
docker_cp(container_id, src_path, dest_path)
