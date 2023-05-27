First build Docker:
- docker build -t my-flask-app .

Secondlyr run Docker:
- docker run -p 5000:5000 my-flask-app

To stop Docker container:
- docker ps
- docker stop <container_id_or_name>
