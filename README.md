# Spendaro

Helping make finance easier for couples one budget at a time.

![Spendaro](./spendaro.png)

## About The Project

Spendaro is a budgeting app that is designed to help couples manage their finances together. As a newlywed, I know just how hard it is to manage finances with your significant other. This app is designed to help make that process easier. Finance and budgeting are a passion of mine and I hope to help others with this app.

## Built With
* React _and other frontend tools and libraries_
* FastAPI
* Docker
* Kubernetes
* AWS
* Github Actions for CI/CD

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

## Features

Under development
