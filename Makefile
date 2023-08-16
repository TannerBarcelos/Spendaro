image:
	$(MAKE) -C spendaro image-dev
container:
	$(MAKE) -C spendaro container-dev
imageprod:
	$(MAKE) -C spendaro image-prod
compose-up:
	$(MAKE) -C spendaro compose-up
compose-down:
	$(MAKE) -C spendaro compose-down
prune:
	$(MAKE) -C spendaro prune
docker-up:
	$(MAKE) image
install-local-deps:
	$(MAKE) -C scripts deps
runclient:
	$(MAKE) -C scripts client
runserver:
	$(MAKE) -C scripts server