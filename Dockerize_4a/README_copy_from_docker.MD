
1. Read Container ID with: 
        read_container_id.py
2. copy file from Docker container: 
        docker cp <container_id>:<container_path> <host_path>
        e.g. docker cp 26caefee6115:/app/data.csv .
        
        e.g. docker cp ac0d7814f5e1:/app/write_csv1.csv .
