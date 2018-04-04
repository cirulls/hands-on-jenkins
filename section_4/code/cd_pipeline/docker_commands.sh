# prefix commands with sudo if user is not in docker group
# build docker image
docker build -t hands-on-jenkins/myapp .

# check docker image
docker images | grep hands-on-jenkins/myapp

# run docker container
docker run -p 8888:5000 --name myapp hands-on-jenkins/myapp 
