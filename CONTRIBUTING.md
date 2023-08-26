## Setup
The quickest way to get started is to use Docker Compose. This will build the images and create the containers for you. You will need to have [Docker](https://www.docker.com/) installed on your machine to proceed with this method.

## Running the app

#### Docker Compose
```bash
Make compose-up
```

#### Local
* This will run the react app and the rest api as standalone services. 
* You will need to have [Node](https://nodejs.org/en/) installed on your machine to proceed with the local route as well as Python3
```bash
Make install-local-deps # Install dependencies for the client and server
Make runclient
Make runserver
```

> The client will be available at `http://localhost:5173`