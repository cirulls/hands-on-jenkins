## Section 4: Exercises

### Theory

1. What is meant by Pipeline as Code and Infrastructure as Code? 

2. What are the benefits of using pipelines over normal build jobs in Jenkins? 

3. What is a Jenkinsfile? 

4. What are the differences between a declarative pipeline and a scripted pipeline? 

5. What is the difference between a Docker image and a Docker container?


### Practice

1. Update the pipeline as follows:

    - Instead of using cat gifs in the web application, use dogs (or your favourite pet!). Amend the Python code of the web application with the new gifs links. For example, you can take funny gifs of dogs from [this URL](https://giphy.com/explore/dogs): click on the image, then select `Copy link` and copy the URL under `GIF Link`. 
    - Change the ports so that the dev environment is deployed at port 8880 and the staging environment at port 8800.

    - If you are familiar with Python and/or shell scripting, add a unit test to the Python test suite and/or an acceptance test to the shell script. 

    - Add a new step to the pipeline. If you are familiar with Docker and have access to a private Docker registry, push the image generated in the Build stage to your Docker registry. For doing this, you need to set the credentials to access the Docker registry and use the pipeline step `docker.withRegistry` (here is an [example for the declarative pipeline](https://jenkins.io/doc/book/pipeline/docker/#custom-registry)).

2. Jenkins X is a new development of Jenkins for building CI/CD solutions for modern cloud applications on Kubernetes. If you use containers and container orchestrators like Kubernetes [check it out](https://jenkins.io/blog/2018/03/19/introducing-jenkins-x/).  
