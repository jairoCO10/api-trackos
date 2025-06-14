# TrackOS API

A simple Jira-like API using FastAPI, MySQL and Docker.

## Development

Create `.env` with your MySQL credentials:

```
MYSQL_USER=user
MYSQL_PASSWORD=pass
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=apidb
SECRET_KEY=change_me
```

Build and run:

```
docker build -t trackos .
docker run -p 8000:8000 --env-file .env trackos
```

The API exposes registration and login endpoints returning JWT tokens, and allows management of organizations and projects with basic roles.
