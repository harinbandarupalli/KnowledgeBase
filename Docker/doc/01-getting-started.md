# Section 1: Getting Started

## 1. What Is Docker?

Docker is a platform that lets you package your application and its dependencies into a **container** — a lightweight, portable unit that runs consistently on any machine.

- **Image** — A blueprint/template for creating containers (read-only).
- **Container** — A running instance of an image.
- **Docker Engine** — The runtime that builds and runs containers.

```
Dockerfile  ──►  Docker Image  ──►  Running Container
(blueprint)      (template)         (live instance)
```

---

## 2. Why Docker & Containers?

**Without Docker:** "It works on my machine" — different environments, dependency conflicts, complex setup.

**With Docker:** Each app runs in its own isolated container with all its dependencies bundled in. Same behavior everywhere.

---

## 3. Virtual Machines vs Docker Containers

| | Virtual Machine | Docker Container |
|--|----------------|-----------------|
| **OS** | Full Guest OS per VM | Shares host OS kernel |
| **Boot time** | Minutes | Seconds |
| **Size** | GBs | MBs |
| **Performance** | Overhead from hypervisor | Near-native |
| **Isolation** | Hardware-level | Process-level |

> Containers are **not** lightweight VMs — they are isolated processes sharing the host kernel.

---

## 4. Docker Setup – macOS

1. Download **Docker Desktop** from [docker.com](https://www.docker.com/products/docker-desktop/)
2. Open `.dmg` → drag Docker to Applications
3. Launch Docker.app → wait for the 🐳 icon in the menu bar
4. Verify:

```bash
docker --version
docker run hello-world
```

---

## 5. Docker Setup – Windows

### Prerequisites
- Windows 10/11 (64-bit)
- WSL 2 enabled
- Hardware virtualization enabled in BIOS

### Steps

1. **Enable WSL 2:**
```powershell
wsl --install
# Restart your computer
```

2. **Install Docker Desktop** from [docker.com](https://www.docker.com/products/docker-desktop/)
   - Check **"Use WSL 2 instead of Hyper-V"** during installation

3. **Verify:**
```powershell
docker --version
docker run hello-world
```

---

## 6. Docker Playground

No installation needed — use [Play with Docker](https://labs.play-with-docker.com/) in your browser (sessions last 4 hours).

---

## 7. Docker Tools Overview

| Tool | Purpose |
|------|---------|
| **Docker CLI** | Build, run, manage containers (`docker` command) |
| **Docker Compose** | Run multi-container apps from a YAML file |
| **Docker Hub** | Cloud registry to share/pull images ([hub.docker.com](https://hub.docker.com/)) |
| **Docker Desktop** | GUI + CLI bundle for local development |

---

## 8. Essential Commands

```bash
# Images
docker pull <image>          # Download an image
docker images                # List local images
docker rmi <image>           # Remove an image

# Containers
docker run <image>           # Run a container
docker run -d -p 8080:80 nginx   # Run in background with port mapping
docker ps                    # List running containers
docker ps -a                 # List all containers
docker stop <container>      # Stop a container
docker rm <container>        # Remove a container
docker logs <container>      # View container logs
docker exec -it <container> /bin/bash  # Open shell inside container
```

### Common Flags

| Flag | Meaning |
|------|---------|
| `-d` | Detached mode (background) |
| `-it` | Interactive terminal |
| `-p 8080:80` | Map host port 8080 → container port 80 |
| `--name` | Name the container |
| `--rm` | Auto-remove container after it exits |

---

## 9. Getting Hands Dirty — First Container

```bash
# Run an Nginx web server
docker run -d -p 8080:80 --name my-nginx nginx
# Visit http://localhost:8080

# Check it's running
docker ps

# View logs
docker logs my-nginx

# Clean up
docker stop my-nginx
docker rm my-nginx
```

---

## 10. Recommended IDE Setup

- Install **VS Code** → Extensions → search **"Docker"** (by Microsoft) → Install
- Gives syntax highlighting, IntelliSense, and container management for Dockerfiles.

---

## Resources

| Resource | Link |
|----------|------|
| Docker Docs | [docs.docker.com](https://docs.docker.com/) |
| Docker Hub | [hub.docker.com](https://hub.docker.com/) |
| Play with Docker | [labs.play-with-docker.com](https://labs.play-with-docker.com/) |
