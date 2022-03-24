# Test Task DevelopsToday REST API Application

# Setup

## Mandatory steps
1. Install Python3.9+
2. Install Pipenv

## Setup project
Install environment
```bash
# Create virtual environment
pip install pipenv

#pipenv install --dev
pipenv shell
```

## Run Project in Docker
```bash
docker-compose up -d 
```

## Formatting code
```bash
# Black
pip install black
python -m black

# Flake8
flake8 .
```

## Postman
### Links: 
http://0.0.0.0:8000/posts/

http://0.0.0.0:8000/posts/id/

http://0.0.0.0:8000/comments/

http://0.0.0.0:8000/comments/id/

http://0.0.0.0:8000/upvote/