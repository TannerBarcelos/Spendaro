# Spendaro

Empowering Your Financial Future: Navigate, Save, Thrive with Spendaro

![Spendaro](./spendaro.png)

> This design is a work in progress. It is not yet functional nor finished.

### Installation
> This project leverages containers to run the application. You will need to have [Docker](https://www.docker.com/) installed on your machine to proceed with the Docker route.
>
> Also be sure to set environment variables for both the client and api directories.
> Please see `.env.local.example` files in both the `api` and `client` folders for any required variables you will need to use based on your usage needs.
> **Be sure to rename the files to `env.local` so they get picked up.** 

**To configure and run Spendaro, enter the following command**
> The client will be available at `http://localhost:5173`
```bash
Make compose-up
```

> Please note that using `docker compose` is the desired way to conveniently, quickly and properly build and run Spendaro. 
> 
> If you wish to run the backend and frontend as standalone images OR not use Docker at all (**highly discouraged as this application is Built, Tested and Deployed to the cloud in Kubernetes**)
> then you must simply edit your `.env.local` file, uncommenting the `VITE_PROXY_LOCAL_URL`
> and then comment out the previously uncommented variable `VITE_PROXY_DOCKER_URL`.
> This change will ensure the React UI can properly proxy API calls between its server and the FastAPI REST web server. 
> Because Docker Compose reauires api calls between containers to call thd service name and not localhost, 
> this configuration is needed to ensure that the right server target is called based on the environment.


### About The Project
Spendaro is a full-featured finance management app. It allows users to create and manage a zero-based budget, organize transactions by category, and generate spending and income reports _with many more things to come_!

### Features
Under development