TRAVIS_REPO_SLUG ?= fernandoe/fe-task-server
TAG ?= local

build:
	docker build -t '${TRAVIS_REPO_SLUG}:${TAG}' .

runserver:
	cd src; python manage.py runserver

migrate:
	cd src; python manage.py migrate

makemigrations:
	cd src; python manage.py makemigrations

test:
	cd src; pytest -s

travis.test:
	docker run --rm -it '${TRAVIS_REPO_SLUG}:${TAG}' pytest -s
