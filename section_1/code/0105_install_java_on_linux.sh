# add PPA repo
sudo add-apt-repository ppa:openjdk-r/ppa

# Install OpenJDK
sudo apt-get update
sudo apt-get install openjdk-8-jdk

# Switch to Java 8
sudo update-alternatives --config java

# Check Java installation
java -version
