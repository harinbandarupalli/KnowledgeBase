# Section 7: Working with "Utility Containers" & Executing Commands

## 1. What Are Utility Containers?

Utility containers don't run an application — they exist to **run tools and commands** (e.g., `npm init`, `composer install`) without installing those tools on your host machine.

```
Traditional:  Install Node.js → run npm init
Utility:      docker run -it node npm init  (no local install needed)
```

---

## 2. Why Use Utility Containers?

- Don't need to install Node, PHP, Python, etc. on your machine
- Lock tools to specific versions
- Consistent tooling across the team
- Great for scaffolding projects

---

## 3. Different Ways of Running Commands in Containers

```bash
# Override the default command
docker run -it node npm init

# Execute a command in a running container
docker exec -it <container> npm install express

# Use ENTRYPOINT for flexible commands
docker run mycli install express
```

---

## 4. Building a Utility Container

```dockerfile
FROM node:18-alpine
WORKDIR /app
```

```bash
docker build -t node-util .
docker run -it -v $(pwd):/app node-util npm init
```

Files created by `npm init` appear on your host via the bind mount.

---

## 5. Utilizing ENTRYPOINT

`ENTRYPOINT` sets a fixed command prefix — anything you pass at `docker run` is **appended** to it.

```dockerfile
FROM node:18-alpine
WORKDIR /app
ENTRYPOINT ["npm"]
```

```bash
# These append to "npm":
docker run -it -v $(pwd):/app node-util init        # runs: npm init
docker run -it -v $(pwd):/app node-util install      # runs: npm install
docker run -it -v $(pwd):/app node-util install express  # runs: npm install express
```

| | `CMD` | `ENTRYPOINT` |
|--|-------|-------------|
| **Overridden by** | `docker run <image> <cmd>` replaces it | Arguments are **appended** to it |
| **Use case** | Default command | Fixed prefix for utility containers |

---

## 6. Using Docker Compose for Utility Containers

```yaml
# docker-compose.yml
version: "3.8"
services:
  npm:
    build: ./
    stdin_open: true
    tty: true
    volumes:
      - ./:/app
    entrypoint: ["npm"]
```

```bash
docker compose run npm init
docker compose run npm install express
```

> `docker compose run` executes a **one-off** command against a service — doesn't start the whole stack.

---

## 7. Permissions & Linux

On Linux, files created by containers may be owned by `root`. Fix with:

```bash
# Run container as your user
docker run -u $(id -u):$(id -g) -v $(pwd):/app node-util npm init
```
