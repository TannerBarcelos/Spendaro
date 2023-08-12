# Variables for Makefile

# Dockerfile name
DOCKERFILE_NAME = Dockerfile.dev

# Docker image and container names
API_IMAGE_NAME = spendaro-rest-image
API_CONTAINER_NAME = spendaro-rest
API_HOST_PORT = 8000
CLIENT_IMAGE_NAME = spendaro-client-image
CLIENT_CONTAINER_NAME = spendaro-client
CLIENT_HOST_PORT = 3000

# Source code locations
CLIENT_LOCATION = spendaro/client
API_LOCATION = spendaro/api

build-client-image:
	cd ${CLIENT_LOCATION} && docker build -t ${CLIENT_IMAGE_NAME} -f ${DOCKERFILE_NAME} .
run-client-container:
	docker run --name ${CLIENT_CONTAINER_NAME} -dp ${CLIENT_HOST_PORT}:3000 ${CLIENT_IMAGE_NAME}
build-api-image:
	cd ${API_LOCATION} && docker build -t ${API_IMAGE_NAME} -f ${DOCKERFILE_NAME} .
run-api-container:
	docker run --name ${API_CONTAINER_NAME} -dp ${API_HOST_PORT}:8000 ${API_IMAGE_NAME}
compose:
	docker-compose up -d --build
compose-down:
	docker-compose down
docker-logs-api:
	docker logs ${API_CONTAINER_NAME}-service-1
docker-logs-client:
	docker logs ${CLIENT_CONTAINER_NAME}-service-1