## Setup

The quickest way to get started is to use Docker Compose. This will build the images and create the containers for you. You will need to have [Docker](https://www.docker.com/) installed on your machine to proceed with this method.

### Running the app with Docker Compose (Recommended)

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

3. Navigate to `http://localhost:5173/` in your browser to view the app. You can also ping the server using a tool like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) at `http://localhost:8000/api/<some_route>`.

### Running the app without Docker Compose

_Note: This method is not recommended as it is more complicated and requires you to have Postgres installed on your machine + other configurations that are not required when using Docker Compose._

**WIP**
