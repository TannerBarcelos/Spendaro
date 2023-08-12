# Non containerized commands
api-install-deps:
	cd api && pip install -r requirements.txt

api-run:
	cd api && uvicorn server:app --reload

client-install-deps:
	cd client && npm install

client-run:
	cd client && npm run dev


# Docker
build-client-image:
	cd client && docker build -t spandaro-client-image -f Dockerfile.dev .
run-client-container:
	docker run --name spendaro-client -dp 3000:3000 spandaro-client-image

build-api-image:
	cd api && docker build -t spendaro-api-image -f Dockerfile.dev .
run-api-container:
	docker run --name spendaro-api -dp 8000:8000 spendaro-api-image

compose:
	docker-compose up -d --build