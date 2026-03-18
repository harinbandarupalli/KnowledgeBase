# Section 2: Docker Images & Containers

## 1. Images & Containers — What and Why?

- **Image** — Contains the code, runtime, libraries, and environment config. It's a **template** — read-only, never changes once built.
- **Container** — A running instance of an image. You can run multiple containers from the same image.

```
  Image (read-only)
    │
    ├──► Container 1 (running)
    ├──► Container 2 (running)
    └──► Container 3 (stopped)
```

---

## 2. Using & Running Pre-Built Images

Docker Hub has thousands of ready-to-use images.

```bash
docker run -it node
docker run -it node:18-alpine
```

---

## 3. Building Your Own Image with a Dockerfile

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

```bash
docker build -t my-node-app .
docker run -p 3000:3000 my-node-app
```

> See code example: [`../code/Dockerfile`](../code/Dockerfile) and [`../code/server.js`](../code/server.js)

---

## 4. EXPOSE & Utility Functionality

- `EXPOSE 3000` in a Dockerfile is **documentation only** — you still need `-p` when running:

```bash
docker run -p 3000:3000 my-node-app
```

---

## 5. Images Are Read-Only

Once built, images **cannot be changed**. Modify code → **rebuild** the image.

```bash
docker build -t my-node-app .
docker run -p 3000:3000 my-node-app
```

---

## 6. Understanding Image Layers

Each Dockerfile instruction creates a **layer**. Docker **caches** unchanged layers.

```dockerfile
FROM node:18-alpine        # Layer 1 (cached)
WORKDIR /app               # Layer 2 (cached)
COPY package.json .        # Layer 3 (cached if unchanged)
RUN npm install            # Layer 4 (cached if package.json unchanged)
COPY . .                   # Layer 5 (rebuilds on code change)
CMD ["node", "server.js"]  # Layer 6
```

> **Tip:** Copy `package.json` before `COPY . .` so dependencies are only reinstalled when `package.json` changes.

---

## 7. Managing Images & Containers

```bash
docker images                  # List images
docker rmi <image_id>          # Remove image
docker image prune             # Remove unused images
docker ps                      # Running containers
docker ps -a                   # All containers
docker rm <container_id>       # Remove container
docker container prune         # Remove all stopped
```

---

## 8. Stopping & Restarting Containers

```bash
docker stop <name>    # Stop
docker start <name>   # Restart (existing container)
```

- `docker run` = creates a **new** container
- `docker start` = restarts an **existing** stopped container

---

## 9. Attached & Detached Containers

| Mode | Behavior | Flag |
|------|----------|------|
| **Attached** (default) | Terminal shows output | (none) |
| **Detached** | Runs in background | `-d` |

```bash
docker run my-node-app              # attached
docker run -d my-node-app           # detached
docker attach <name>                # re-attach
docker logs -f <name>               # follow logs
```

---

## 10. Entering Interactive Mode

```bash
docker run -it python                       # interactive
docker exec -it <container> /bin/sh         # shell into running container
```

| Flag | Meaning |
|------|---------|
| `-i` | Keep STDIN open |
| `-t` | Allocate a pseudo-TTY |

---

## 11. Deleting Images & Containers

```bash
docker rm <container>           # Remove container
docker rmi <image>              # Remove image
docker container prune          # Remove all stopped containers
docker image prune -a           # Remove all unused images
```

---

## 12. Removing Stopped Containers Automatically

```bash
docker run --rm -p 3000:3000 my-node-app
# Container auto-removed when stopped
```

---

## 13. Inspecting Images

```bash
docker image inspect <image_id>
```

---

## 14. Copying Files Into & From a Container

```bash
docker cp <container>:/path ./local/path    # FROM container
docker cp ./local/file <container>:/path    # TO container
```

---

## 15. Naming & Tagging

```bash
docker run --name my-app my-node-app       # Name a container
docker build -t my-app:v1 .               # Tag an image
docker tag my-app:v1 myuser/my-app:v1     # Retag
```

Format: `name:tag` — e.g., `node:18-alpine`, `my-app:latest`

---

## 16. Sharing Images — Docker Hub

```bash
# Push
docker login
docker tag my-app:latest yourusername/my-app:latest
docker push yourusername/my-app:latest

# Pull
docker pull yourusername/my-app:latest
docker run yourusername/my-app:latest
```
