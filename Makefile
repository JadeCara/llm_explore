BLACK := black --check .
FLAKE8 := flake8 .

# Docker
build:
	docker-compose up --build -d

down:
	docker compose down

prune:
	docker system prune -a

# Linting
.PHONY: lint
lint:
	$(BLACK)
	$(FLAKE8)

.PHONY: format
format:
	black .

.PHONY: flake8
flake8:
	$(FLAKE8)

.PHONY: black
black:
	$(BLACK)
