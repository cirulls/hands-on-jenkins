# Add yum repo and install Jenkins
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
sudo rpm --import http://pkg.jenkins-ci.org/redhat-stable/jenkins-ci.org.key
sudo yum install jenkins

# Start Jenkins at boot time
sudo systemctl start jenkins.service
sudo systemctl enable jenkins.service
