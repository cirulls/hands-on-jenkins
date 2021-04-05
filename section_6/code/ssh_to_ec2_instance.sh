# ssh into EC2 instance (replace key name and hostname)  
ls -lah /path/jenkins-key.pem
chmod 400 /path/jenkins-key.pem
ssh -i /path/jenkins-key.pem ec2-user@ec2-123-456-78-9.compute-1.amazonaws.com  
