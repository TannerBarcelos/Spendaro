# Spendaro

Helping make finance easier for couples one budget at a time.

![Spendaro](./spendaro.png)

## About The Project

Spendaro is a budgeting app that is designed to help couples manage their finances together. It is built using React for the frontend and FastAPI for the backend. The app is designed to be run locally or in a containerized environment. The app is designed to be deployed to a cloud provider such as AWS.

## Setup
The quickest way to get started is to use Docker Compose. This will build the images and create the containers for you. You will need to have [Docker](https://www.docker.com/) installed on your machine to proceed with this method.

## Running the app

#### Docker Compose
```bash
Make compose-up
```

> **IMPORTANT**
> If you wish to run the backend and frontend as standalone images or not use Docker at all in development, you will need to change a configuration setting in the `./spendaro/client` directory. The setting is `withService` and it should be set to false if you plan to run locally.


#### Local
* This will run the react app and the rest api as standalone services. 
* You will need to have [Node](https://nodejs.org/en/) installed on your machine to proceed with the local route as well as Python3
```bash
Make install-local-deps # Install dependencies for the client and server
Make runclient
Make runserver
```

> The client will be available at `http://localhost:5173`

## Features

Under development
