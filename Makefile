TRAVIS_REPO_SLUG ?= fernandoe/fe-task-server
TAG ?= local

docker-build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

runserver:
	cd src; python manage.py runserver

migrate:
	cd src; python manage.py migrate

test:
	cd src; pytest -s

travis.test:
	test
