# Section 3: Managing Data & Volumes

## 1. Understanding Data Categories

| Type | Stored Where | Survives Container Removal? |
|------|-------------|---------------------------|
| **Application Code** | Image (read-only layer) | Yes (in the image) |
| **Temporary Data** | Container layer (read-write) | ❌ No |
| **Permanent Data** | Volumes / Bind Mounts | ✅ Yes |

**The Problem:** `docker rm` deletes all data inside the container. Volumes solve this.

---

## 2. Introducing Volumes

Volumes are folders on the **host machine** mapped into the container. Data **persists** after container removal.

### Types of Volumes

| Type | Created By | Host Path Known? | Use Case |
|------|-----------|-------------------|----------|
| **Anonymous Volume** | Docker (auto) | No | Temp data, caching |
| **Named Volume** | `-v name:/path` | No | Persistent app data (DB, uploads) |
| **Bind Mount** | `-v /host:/container` | Yes | Development — live code sharing |

---

## 3. Anonymous Volumes

```dockerfile
VOLUME ["/app/data"]
```
```bash
docker run -v /app/data my-app
```

---

## 4. Named Volumes

```bash
docker run -v my-data:/app/data my-app
# Data survives container removal
```

---

## 5. Removing Anonymous Volumes

```bash
docker volume ls
docker volume rm <volume_name>
docker volume prune
```

---

## 6. Bind Mounts (Code Sharing)

```bash
# macOS/Linux
docker run -v $(pwd):/app my-app

# Windows PowerShell
docker run -v "${PWD}:/app" my-app
```

---

## 7. Combining & Merging Different Volumes

```bash
docker run \
  -v $(pwd):/app \
  -v /app/node_modules \
  -v my-data:/app/data \
  -p 3000:3000 my-app
```

> Anonymous volume for `node_modules` prevents the bind mount from overwriting it.

---

## 8. Using Nodemon in a Container

```json
{ "scripts": { "start": "nodemon server.js" } }
```
```bash
docker run -v $(pwd):/app -v /app/node_modules -p 3000:3000 my-app
```

---

## 9. Read-Only Volumes

```bash
docker run -v $(pwd)/src:/app/src:ro my-app
```

---

## 10. Managing Docker Volumes

```bash
docker volume ls
docker volume inspect my-data
docker volume rm my-data
docker volume prune
```

---

## 11. COPY vs Bind Mounts

| | `COPY` (Dockerfile) | Bind Mount (`-v`) |
|--|---------------------|-------------------|
| **When** | Build time | Run time |
| **Production** | ✅ Yes | ❌ No |
| **Development** | Needed for build | ✅ Use for live reload |

---

## 12. Using .dockerignore

```
node_modules
.git
Dockerfile
.dockerignore
.env
npm-debug.log
```

---

## 13. Environment Variables & .env Files

```dockerfile
ENV PORT=3000
EXPOSE $PORT
```

```bash
docker run -e PORT=8080 my-app
docker run --env-file ./.env my-app
```

> ⚠️ Never put secrets in `ENV` in Dockerfile — use `--env-file` instead.

---

## 14. Using Build Arguments (ARG)

```dockerfile
ARG DEFAULT_PORT=3000
ENV PORT=$DEFAULT_PORT
```

```bash
docker build --build-arg DEFAULT_PORT=8080 -t my-app .
```

| | `ARG` | `ENV` |
|--|-------|-------|
| **Available during** | Build only | Build + Runtime |
| **Set via** | `--build-arg` | `-e` / `--env-file` |
| **In running container?** | ❌ No | ✅ Yes |
