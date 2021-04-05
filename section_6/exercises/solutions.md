## Section 6: Solutions to Exercises

### Theory

1. The master/slave configuration allows to distribute builds in Jenkins and this has advantages in terms of:

    - Flexibility: the slave nodes can be customized to run specific jobs (for example build and test on a specific browser or operating system). 
    - Resilience: the performance on the master node is improved as long running and resource consuming jobs are sent to slave nodes. Plus, even if a slave node fails, jobs running on other nodes are not affected. 
    - Scalability: slave nodes free resources from the master node, allow to run jobs in parallel thus sharing the load across multiple machines, and scale automatically since the number of slave nodes is increased at peak build times and decreased during low activity times.  

2. In a single master configuration Jenkins is deployed on a single, large master with multiple slave nodes connected to it. In a multiple master configuration Jenkins is deployed on multiple smaller masters with multiple slave nodes connected to each other. 

    A single master configuration is easier to maintain and is well suited for a single team whereas the multi master configuration is more robust and is better suited for multiple teams.
 
3. VPC stands for virtual private cloud  and is an isolated virtual network inside AWS. It is a good security practice to launch AWS resources inside a VPC so that they are isolated from other projects deployed on AWS. 

4. A security group is a virtual firewall for controlling inbound and outbound traffic to resources in a VPC.

5. IAM stands for Identity and Access Management and it enables to access AWS services and resources securely. In particular, IAM is used to create users, permissions, and roles. 

    A IAM policy is a set of permissions usually attached to a user or a resource. IAM policies are expressed and stored as JSON files. 

### Practice

1. To create a new slave node, add a new AMI in `Manage Jenkins` -> `Configure System` -> `Cloud` -> `Amazon EC2` -> `AMIs` -> `Add`. You can copy the same configuration used in video 6.4 but under `Labels` use a different label. Then create a new Jenkins job and in General thick the option `Restrict where this project can be run` and type in `Label expression` the label given to the new slave.
