install-local-deps:
	$(MAKE) -C scripts deps
runclient:
	$(MAKE) -C scripts client
runserver:
	$(MAKE) -C scripts server

# Docker Compose commands
compose-up:
	docker-compose -f ./docker/docker-compose.dev.yaml -p spendaro up -d 
compose-up-prod:
	docker-compose -f ./docker/docker-compose.prod.yaml -p spendaro-prod up -d 
compose-up-tests:
	docker-compose -f ./docker/docker-compose.tests.yaml -p spendaro-tests up -d
compose-down:
	docker-compose -f ./docker/docker-compose.dev.yaml down
compose-down-prod:
	docker-compose -f ./docker/docker-compose.prod.yaml down
compose-down-tests:
	docker-compose -f ./docker/docker-compose.tests.yaml down

# Docker commands (non-compose)
image-dev:
	$(MAKE) -C spendaro image-dev
container-dev:
	$(MAKE) -C spendaro container-dev
image-prod:
	$(MAKE) -C spendaro image-prod
container-prod:
	$(MAKE) -C spendaro container-prod
prune:
	$(MAKE) -C spendaro prune
docker-up:
	$(MAKE) image