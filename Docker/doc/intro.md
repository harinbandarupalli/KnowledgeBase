# 🐳 Docker — Complete Course Documentation

A concise reference guide for Docker, from basics to deployment.

---

## Table of Contents

| # | Section | Topics | File |
|---|---------|--------|------|
| 1 | **Getting Started** | What is Docker, Setup (macOS/Windows), Essential Commands, First Container | [01-getting-started.md](01-getting-started.md) |
| 2 | **Images & Containers** | Dockerfile, Layers & Caching, Interactive Mode, Naming & Tagging, Docker Hub | [02-images-and-containers.md](02-images-and-containers.md) |
| 3 | **Managing Data & Volumes** | Volumes, Bind Mounts, .dockerignore, ENV, ARG | [03-data-and-volumes.md](03-data-and-volumes.md) |
| 4 | **Networking** | Container ↔ WWW, Host, Container Communication, Docker Networks, Drivers | [04-networking.md](04-networking.md) |
| 6 | **Docker Compose** | Compose Files, Up/Down, Multi-Container Apps, Build & Naming | [06-docker-compose.md](06-docker-compose.md) |
| 7 | **Utility Containers** | Running Commands, ENTRYPOINT, Compose for Tools, Permissions | [07-utility-containers.md](07-utility-containers.md) |
| 8 | **Complex Setup (Laravel)** | Nginx + PHP + MySQL, Utility Containers, Bind Mounts vs COPY | [08-complex-setup-laravel.md](08-complex-setup-laravel.md) |
| 9 | **Deploying Containers** | EC2, ECS, Managed DBs, Multi-Stage Builds, Production Best Practices | [09-deploying-containers.md](09-deploying-containers.md) |

---

## Section Summaries

### 1. Getting Started
Docker packages apps into **containers** — lightweight, portable units. Install Docker Desktop, learn essential CLI commands, and run your first Nginx container.

### 2. Images & Containers
Images are **read-only templates** built from Dockerfiles. Containers are running instances. Learn to build, tag, share via Docker Hub, and manage the full lifecycle.

### 3. Managing Data & Volumes
Container data is **lost on removal**. Use **Named Volumes** for persistent data, **Bind Mounts** for development, and `.dockerignore` + `ENV`/`ARG` for configuration.

### 4. Networking
Containers can talk to the **internet** (automatic), the **host** (`host.docker.internal`), and **other containers** (via Docker Networks with DNS-based name resolution).

### 6. Docker Compose
Define multi-container apps in a single `docker-compose.yml`. One command (`docker compose up`) replaces dozens of `docker run` flags. Handles networks, volumes, and build.

### 7. Utility Containers
Run tools like `npm`, `composer`, or `artisan` inside containers **without installing them locally**. Use `ENTRYPOINT` for flexible utility images.

### 8. Complex Setup — Laravel & PHP
A real-world multi-container project: **Nginx** (web server) + **PHP-FPM** (application) + **MySQL** (database), plus utility containers for Composer, Artisan, and npm.

### 9. Deploying Containers
Move from development to production. Deploy manually on **AWS EC2**, or use managed services like **AWS ECS**. Use **multi-stage builds** for smaller images and **managed databases** in production.

---

## Quick Reference

```bash
# Build & Run
docker build -t my-app .
docker run -d -p 3000:3000 --name app my-app

# Compose
docker compose up -d --build
docker compose down -v

# Cleanup
docker system prune -a
```

## Resources

| Resource | Link |
|----------|------|
| Docker Docs | [docs.docker.com](https://docs.docker.com/) |
| Docker Hub | [hub.docker.com](https://hub.docker.com/) |
| Docker Compose Docs | [docs.docker.com/compose](https://docs.docker.com/compose/) |
| Play with Docker | [labs.play-with-docker.com](https://labs.play-with-docker.com/) |
