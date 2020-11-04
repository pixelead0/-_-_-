# Django BeautifulSoup Example

This project implements a example of BeautifulSoup with django

Author: pixelead0
email: adangq@gmail.com

## Requirements:

- [Docker](https://docs.docker.com/engine/installation/).
- [Docker-compose](https://docs.docker.com/compose/install).

## Technologies

- `Python 3.8`
- `Django 1.1.2 `
- `Docker`
- `PostgreSQL 11`

## COLLABORATIVE WORKFLOW

1. Before beginning any work, always pull latest version of `dev`
   branch.
2. Create a new branch from `master`. There are two formats for branch names:
   1. `github_username/description_of_feature/trello_id`
      Use this format when an associated Trello ticket exists for this
      particular feature that you are working on.
   2. `github_username/description_of_feature`
      Use this format where there is not an associated Trello ticket
      for the particular feature that you are working on.
      Some example branch names:
   - `pixelead0/changes-button-colors`
   - `pixelead0/fixes-login-error/xeuoiu37893`
3. Do your work in the new feature branch that you made.
4. When the branch is ready, rebase all your changes into one commit.
   - Make sure commit has a descriptive title in all title case.
     For example:
     `Changes Button Colors`
   - Add the bottom of each commit message, if there is a trello ticket,
     post the ticket url like this:
     `Reference: https://trello.com/blah/blah/113873`
5. Push your branch up to Github
6. Make a new Pull Request from your feature branch to the `master` branch.
   Never push directly into the `master` branch.
   1. In the PR, add `pixelead0` as a reviewer
7. Notify `pixelead0` that PR is ready for review.

## INITIAL IDE SETUP

You will probably need to build some files for your IDE. These
will only be accessed by the IDE. These are not used by the actual app server. The app server uses the files which are inside the docker container.

On your host machine, setup python environment:

```shell
# FROM HOST
rm -fr ./venv
virtualenv -p python3.8 ./venv
./venv/bin/pip3 install -r ./api/requirements.txt
```

## Install:

**Clone the repository**

```shell
git clone git@github.com:pixelead0/django_order_system.git
```

**Copy the configuration files.**

```shell
sh config-init.sh
```

**Run docker-compose to start the containers:**

```shell
docker-compose up
```

**Reset own files user**

```shell
sudo chown -R $USER
```

**Export local database to fixtures**

Add new fixture to `generate_fixtures.sh` file and reganerate the fixtures

```shell
sh generate_fixtures.sh
```

**Load data to local database**

Edit `api/load_fixtures.sh` and rebuild api container.

```shell
docker-compose --build api
```

**Reload data to local database without build container**

Edit `api/load_fixtures.sh` and execute:

```shell
sh reload_fixtures.sh
```

---

# Docker commands

## Delete all containers

```
docker-compose rm -fsa
```

## Containers init

```
docker-compose up
```

## Restart only python container

```
docker-compose restart api
```
