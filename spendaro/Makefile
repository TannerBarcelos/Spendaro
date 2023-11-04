# API variables
API_IMAGE_NAME=spendaro-api
API_CONTAINER_NAME=api-service
API_HOST_PORT=8000

# Client variables
CLIENT_IMAGE_NAME=spendaro-client
CLIENT_CONTAINER_NAME=client-service
CLIENT_HOST_PORT=5173

# DB variables
DB_IMAGE_NAME=postgres
DB_CONTAINER_NAME=db-service

TARGET_STAGE_DEV=dev
TARGET_STAGE_PROD=prod

# Build and run the containers for development
image-dev:
	docker build -t ${CLIENT_IMAGE_NAME} --target ${TARGET_STAGE_DEV} ./client
	docker build -t ${API_IMAGE_NAME} --target ${TARGET_STAGE_DEV} ./api

container-dev:
	docker run --name ${CLIENT_CONTAINER_NAME} -v $(PWD)/spendaro/client:/usr/app -v /usr/app/node_modules -dp ${CLIENT_HOST_PORT}:5173 ${CLIENT_IMAGE_NAME}
	docker run --name ${API_CONTAINER_NAME} -v $(PWD)/spendaro/api:/usr/api -dp ${API_HOST_PORT}:8000 ${API_IMAGE_NAME}
	docker run --name ${DB_CONTAINER_NAME} -e POSTGRES_PASSWORD=postgres -dp 5432:5432 ${DB_IMAGE_NAME}


# Build and run the containers for production
image-prod:
	docker build -t ${CLIENT_IMAGE_NAME} --target ${TARGET_STAGE_PROD} ./client
	docker build -t ${API_IMAGE_NAME} --target ${TARGET_STAGE_PROD} ./api

container-prod:
	docker run --name ${CLIENT_CONTAINER_NAME} -dp ${CLIENT_HOST_PORT}:80 ${CLIENT_IMAGE_NAME}
	docker run --name ${API_CONTAINER_NAME} ${API_HOST_PORT}:8000 ${API_IMAGE_NAME}
	docker run --name ${DB_CONTAINER_NAME} -e POSTGRES_PASSWORD=postgres -dp 5432:5432 ${DB_IMAGE_NAME}


docker-logs-api:
	docker logs ${API_CONTAINER_NAME}-service-1

docker-logs-client:
	docker logs ${CLIENT_CONTAINER_NAME}-service-1

prune:
	docker system prune -a
