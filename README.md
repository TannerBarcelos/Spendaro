# Spendaro

Empowering Your Financial Future: Navigate, Save, Thrive with Spendaro

![Spendaro](./spendaro.png)

> This design is a work in progress. It is not yet functional nor finished.

### About The Project

Spendaro is a full-featured finance management app. It allows users to create and manage a zero-based budget, organize transactions by category, and generate spending and income reports _with many more things to come_!

### Setup

You will need to have [Docker](https://www.docker.com/) installed on your machine to proceed with the Docker route.

**Run using Docker Compose**
```bash
Make compose-up
```

> **IMPORTANT**
> If you wish to run the backend and frontend as standalone images or not use Docker at all in development, you will need to change a configuration setting in the [client](./spendaro/client). The setting is `withService` and it should be set to false if you plan to run locally.

**Run using Docker**
```bash
Make image # Build the images 
Make container # Create the containers
```
**Run Locally**
> This will run the react app and the rest api as standalone services. You will need to have [Node](https://nodejs.org/en/) installed on your machine to proceed with the local route as well as Python3
```bash
Make runclient
Make runserver
```

The client will be available at `http://localhost:5173`

### Features

Under development
