# Section 6: Docker Compose — Multi-Container Orchestration

## 1. What Is Docker Compose & Why?

Managing multiple `docker run` commands with long flags is tedious. **Docker Compose** lets you define all your services, networks, and volumes in a single `docker-compose.yml` file.

**Without Compose:**
```bash
docker network create my-net
docker run -d --name mongodb --network my-net -v data:/data/db mongo
docker run -d --name app --network my-net -p 3000:3000 -e MONGO_URL=mongodb://mongodb:27017/mydb my-app
```

**With Compose:** One file, one command.

---

## 2. Creating a Compose File

```yaml
# docker-compose.yml
version: "3.8"

services:
  mongodb:
    image: mongo
    volumes:
      - data:/data/db

  app:
    build: ./app
    ports:
      - "3000:3000"
    environment:
      - MONGO_URL=mongodb://mongodb:27017/mydb
    depends_on:
      - mongodb

volumes:
  data:
```

---

## 3. Compose File Key Configurations

| Key | Description |
|-----|-------------|
| `image` | Use a pre-built image |
| `build` | Build from a Dockerfile (path to context) |
| `ports` | Port mapping (`host:container`) |
| `volumes` | Named volumes or bind mounts |
| `environment` | Environment variables |
| `env_file` | Load variables from a file |
| `depends_on` | Start order (not readiness) |
| `stdin_open: true` | Equivalent to `-i` |
| `tty: true` | Equivalent to `-t` |
| `container_name` | Custom container name |

---

## 4. Installing Docker Compose

- **Docker Desktop** (Windows/macOS): Already included ✅
- **Linux:**
```bash
sudo apt-get install docker-compose-plugin
# Verify
docker compose version
```

> Note: `docker-compose` (with hyphen) is the legacy v1. Use `docker compose` (space) for v2.

---

## 5. Docker Compose Up & Down

```bash
# Start all services (build if needed)
docker compose up

# Start in detached mode
docker compose up -d

# Rebuild images before starting
docker compose up --build

# Stop and remove containers, networks
docker compose down

# Also remove volumes
docker compose down -v
```

---

## 6. Working with Multiple Containers

Compose creates a **default network** for all services — they can communicate using service names as hostnames.

```yaml
services:
  backend:
    build: ./backend
    ports:
      - "3000:3000"

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  database:
    image: mongo
    volumes:
      - db-data:/data/db

volumes:
  db-data:
```

> Inside `backend`, connect to the database as `mongodb://database:27017/mydb`.

---

## 7. Building Images & Container Names

```bash
# Build or rebuild images
docker compose build

# Start with forced rebuild
docker compose up --build
```

Compose auto-generates container names like `projectfolder-service-1`. Override with `container_name:`.

---

## 8. Compose Commands Summary

```bash
docker compose up              # Start all services
docker compose up -d           # Start detached
docker compose up --build      # Rebuild + start
docker compose down            # Stop + remove
docker compose down -v         # Stop + remove + delete volumes
docker compose build           # Build images only
docker compose logs            # View logs
docker compose ps              # List running services
docker compose run <service>   # Run a one-off command
```
