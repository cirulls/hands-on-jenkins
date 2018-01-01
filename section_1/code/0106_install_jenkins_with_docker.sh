# Pull official Docker image for Jenkins LTS
docker pull jenkins/jenkins:lts

# Start Docker container
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins jenkins/jenkins:lts

# Start Docker container in detached mode
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins -d jenkins/jenkins:lts
