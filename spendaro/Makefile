API_IMAGE_NAME = spendaro-rest-image
API_CONTAINER_NAME = rest-service
API_HOST_PORT = 8000

CLIENT_IMAGE_NAME = spendaro-client-image
CLIENT_CONTAINER_NAME = client-service
CLIENT_HOST_PORT = 5173

TARGET_STAGE_DEV=dev
TARGET_STAGE_PROD=prod

image-dev:
	docker build -t ${CLIENT_IMAGE_NAME} --target ${TARGET_STAGE_DEV} ./client
	docker build -t ${API_IMAGE_NAME} --target ${TARGET_STAGE_DEV} ./api

container-dev:
  	docker run --name ${CLIENT_CONTAINER_NAME} -dp ${CLIENT_HOST_PORT}:5173 ${CLIENT_IMAGE_NAME}
	docker run --name ${API_CONTAINER_NAME} -dp ${API_HOST_PORT}:8000 ${API_IMAGE_NAME}

image-prod:
	docker build -t ${CLIENT_IMAGE_NAME} --build-arg NODE_ENV=production --target ${TARGET_STAGE_PROD} ./client
	docker build -t ${API_IMAGE_NAME} --build-arg NODE_ENV=production --target ${TARGET_STAGE_PROD} ./api

compose-up:
	docker-compose up -d

compose-down:
	docker-compose down

docker-logs-api:
	docker logs ${API_CONTAINER_NAME}-service-1

docker-logs-client:
	docker logs ${CLIENT_CONTAINER_NAME}-service-1

prune:
	docker system prune -a