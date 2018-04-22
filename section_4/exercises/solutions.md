## Section 4: Solutions to Exercises

### Theory

1. The concept of Pipeline as Code refers to a set of features which allow to define and combine job processes using code and to store this code under version control. In other words, Jenkins jobs and their configurations are defined as code instead of manual configuration via the Jenkins graphical user interface. 

    Pipeline as Code falls into the general concept of Infrastructure as Code. The idea behind Infrastructure as Code is that IT infrastructure is managed and provisioned through code rather than manual configuration. 

2. These are some advantages of pipelines compared to normal build jobs in Jenkins:

    - Pipelines are expressed as code and can therefore be stored under version control like any other script.
    - The resilience of a pipeline job is higher since it can survive a Jenkins restart and can be rebuilt from a previous stage. 
    - Pipelines can be paused and wait for a manual approval. 
    - Pipelines are very versatile and can support complex requirements like loops, conditional and matrix processing, and parallelisation of jobs. 
    - Pipelines can be extended via domain-specific language scripts and shared libraries written in Groovy. 
    - Pipelines can be visualized for the benefit of both technical and non-technical people. 

3. A Jenkinsfile is a script containing the definition and the steps to execute a Jenkins pipeline. 

4. A scripted pipeline follows the imperative programming model and is particularly suited for implementing complex requirements thanks to its flexibility and extensibility. In fact, anything that can be scripted in Groovy can be executed in a scripted pipeline. Scripted pipelines are well suited for developers having experience with Groovy or another scripting language.

    A declarative pipeline follows the declarative programming model which focuses on what the pipeline should accomplish without specifying in detail how to perform it. A declarative pipeline is suited for regular requirements due to its pre-defined and opinionated syntax. This makes declarative pipelines more readable.

    Both scripted and declarative pipelines are valid ways to write pipelines in Jenkins.  

5. A Docker image is like a class in object orient programming. In other words, it is a blueprint or a recipe - a way to describe something at a higher level. Conversely, Docker containers are like objects in object-oriented programming. In other words, a Docker container is a concrete instance of a Docker image. 

### Practice

1. See the following files: 

    - [app.py](app.py)
    - [Jenkinsfile](Jenkinsfile)
    - [test_flask_app.py](test_flask_app.py)
    - [Jenkinsfile](Jenkinsfile)
