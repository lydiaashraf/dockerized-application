# Dockerized Multi-Container Application

## Overview

This project extends a simple Python REST API into a multi-container architecture using Docker Compose.

The application consists of three services:

* **Nginx** — Reverse proxy and public entry point
* **FastAPI** — Backend application
* **Redis** — Caching layer

## Architecture

```text
Client / Browser
       |
       v
   Nginx :80
       |
       v
 FastAPI :8000
       |
       v
  Redis :6379
```

Only Nginx is exposed to the host. FastAPI and Redis communicate internally through the Docker Compose network.

## Technologies

* Python
* FastAPI
* Uvicorn
* Docker
* Docker Compose
* Nginx
* Redis

## Project Structure

```text
Dockerized application/
│
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── nginx/
│   └── nginx.conf
│
└── docker-compose.yml
```

## Services

### 1. FastAPI

The FastAPI service contains the backend application.

It listens on port `8000` inside the Docker network.

The application provides API endpoints such as:

* `GET /`
* `GET /cache`

### 2. Redis

Redis is used as an in-memory caching layer.

The FastAPI application connects to Redis using the Docker Compose service name:

```text
redis
```

Redis listens on port `6379` inside the Docker network.

### 3. Nginx

Nginx acts as a reverse proxy and the public entry point.

The host exposes:

```text
localhost:80
```

Nginx forwards requests to the FastAPI service.

## Docker Compose

Docker Compose is used to define and manage the three services.

Start the application:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d
```

Check running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

Stop the application:

```bash
docker compose down
```

## Testing

Open:

```text
http://localhost
```

To test the Redis integration:

```text
http://localhost/cache
```

The `/cache` endpoint stores a value in Redis and retrieves it through the FastAPI application.

## Networking

Docker Compose creates a default internal network for the services.

Services can communicate with each other using their service names.

For example, FastAPI connects to Redis using:

```text
redis:6379
```

No hardcoded container IP addresses are required.

## Port Mapping

Nginx:

```text
Host:80 -> Container:80
```

FastAPI:

```text
Container:8000
```

Redis:

```text
Container:6379
```

FastAPI and Redis are not exposed directly to the host.

## Key Concepts Demonstrated

This project demonstrates:

* Containerization
* Multi-container architecture
* Docker Compose
* Docker networking
* Service discovery
* Reverse proxy
* Redis caching
* Port mapping
* Bind mounts
* Container dependencies
* Troubleshooting Docker services

## Project Evolution

This project is the second step after the Python REST API project.

### Project 1

The first project focused on building and containerizing a simple REST API.

```text
Client
   |
   v
FastAPI
   |
Docker Container
```

### Project 2

The second project makes the architecture more realistic by introducing multiple services.

```text
Client
   |
   v
Nginx
   |
   v
FastAPI
   |
   v
Redis
```

This progression demonstrates the move from a simple single-container application to a multi-container architecture managed with Docker Compose.
