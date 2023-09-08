install-local-deps:
	$(MAKE) -C scripts deps
runclient:
	$(MAKE) -C scripts client
runserver:
	$(MAKE) -C scripts server

# Docker commands
compose-up:
	docker-compose -f ./docker/docker-compose.yaml -p spendaro up -d 
compose-down:
	docker-compose down
image:
	$(MAKE) -C spendaro image-dev
container:
	$(MAKE) -C spendaro container-dev
imageprod:
	$(MAKE) -C spendaro image-prod
prune:
	$(MAKE) -C spendaro prune
docker-up:
	$(MAKE) image