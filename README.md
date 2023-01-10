# Justworks Restaurant
This coding challenge requires designing the API for a restaurant reservation system based on the guidelines on the [Tax Tech Challenge](https://github.com/joinjustworksptu/TaxTechChallenge/blob/main/Backend.md) Gtihub.

Solved by: Gabriel Hruskovec

## Setup
The doc provides suggestions on how to manage and update the required dependencies on MacOS. The environment requirements should be the same in other OSes but use the preferred package manager for that instead. The project can be run directly through the CLI using `uvicorn`, an ASGI server implementation for Python or using Docker.

### CLI with Python
1. `Python 3.10.9`. To update: `$ brew upgrade python`. 
2. Create a virtual environment: `$ python3 -m env env` and activate: `$ source env/bin/activate`. 
3. Install the dependencies: `$ pip install -r requirements.txt`.
4. `VERSION = PostgreSQL 14.6 (Homebrew)`. To install: `$ brew install postgresql`.

### Docker
1. Download Docker from [their site](https://docs.docker.com/desktop/install/mac-install/) and follow the installation guide. That should install the common CLI tools as well.
2. Create a .env file with the postgres connection credentials
2. Build the restaurant server image: `.venv ❯ docker build . -t justworks-restaurant-server`.

## Run

## Tests

## Troubleshooting
If you're having issues running the project, verify that your software is up to date. Below are versions for the dependencies that are confirmed to work, as reference.
- Python 3.11
- Poetry v1.3.1
- Docker v20.10
- Docker Compose v2.13