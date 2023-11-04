## Setup

The quickest way to get started is to use Docker Compose. This will build the images and create the containers for you. You will need to have [Docker](https://www.docker.com/) installed on your machine to proceed with this method.

### Running the app

1. Create a `.env` file in the `docker` directory and add the following variables:

```bash
POSTGRES_USER=<replace_me>
POSTGRES_PASSWORD=<replace_me>
POSTGRES_DB=<replace_me>
POSTGRES_HOST=<replace_me>
POSTGRES_PORT=<replace_me>
```

> These variables are used to spin up the Postgres Database. You can use any values you want for these variables but ensure they are secure.
>
> **Note that if you do not do this step, the application still runs but will be using insecure default values of the above variables where the name of the database is `postgres`, the username is `postgres` and the password is `postgres` and the host is `localhost` and the port is `5432`. _(see `config.py`)_**

2. Set your python path to the root of the project

```bash
cd spendaro/api
export PYTHONPATH=${PYTHONPATH}:$(pwd)
```

2. Run with pre-set Makefile docker compose command

```bash
Make compose-up
```

#### Local

- This will run the react app and the rest api as standalone services **outside of Docker**
- You will need to have [Node](https://nodejs.org/en/) installed on your machine to proceed with the local route as well as Python3

```bash
Make install-local-deps # Install dependencies for the client and server
Make runclient
Make runserver
```
