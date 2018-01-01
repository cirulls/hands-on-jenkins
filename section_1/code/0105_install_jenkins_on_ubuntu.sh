# Add PPA repo for Jenkins stable LTS
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c "echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list"
sudo apt-get update

# Install Jenkins
sudo apt-get install jenkins

# Start Jenkins at boot time
sudo systemctl start jenkins.service
sudo systemctl enable jenkins.service
