## Section 3: Solutions to Exercises

### Theory

1. Continuous Integration (CI) is a software development practice whereby members of a team integrate, build, and test their code frequently in a development environment.

    Continuous Delivery (CD) is a software development practice whereby a team builds software in such a way that it can be released to production at any time.

    Continuous Deployment means that every change automatically gets pushed to production, resulting in many production deployments every day.

2. These are the main components of a typical CI workflow:

    - A source control management (e.g. GitHub)
    - A CI server (e.g. Jenkins)
    - A build tool (e.g. Maven)
    - A notification channel (e.g. emails, Slack, etc.)
    - A repository where to push build artifacts or images (e.g. Nexus) (not used in the demo but often employed)

3. This is a list of typical types of tests:

    - **Unit tests**: test a single unit of code (e.g. a method of a class or a function)
    - **Integration tests**: test the correct interaction between systems (e.g. application and database can communicate)
    - **Acceptance tests**: test that a feature or use case is correctly implemented (also known as end-to-end tests)
    - **Regression tests**: test that a bug is fixed and won’t happen again
    - **Smoke tests**: tests executed before running longer test suites
    - **Load tests**: test the system under load (e.g. heavy traffic) - similar to stress and performance tests
    - **Security tests**: test security issues (e.g. security updates applied)

4. Passive (or pull) notifications require the developer to actively consult the latest build status. Active (or push) notifications proactively alert the developer when something happens.
 
### Practice

1. One of the notification channels I use is the RSS feeds as I find it less intrusive than emails and I can ask any one who is interested in following a build status to subscribe without changing the Jenkins set up. Each build contains a link to subscribe to RSS feeds (for all builds or only for failed builds) on the right hand side below the Build History menu. You can receive RSS feeds in your inbox by configuring your email client or use an RSS feed software or browser plugin. 

