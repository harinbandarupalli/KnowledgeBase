# Section 4: Networking — (Cross-)Container Communication

## 1. Three Communication Cases

| Case | Description | Example |
|------|------------|---------|
| **Container → WWW** | Container talks to the internet | Calling a public API |
| **Container → Host** | Container talks to host machine | App → DB on host |
| **Container → Container** | Container talks to another container | App → DB container |

---

## 2. Container to WWW Communication

**Works out of the box** — no special config needed.

---

## 3. Container to Host Machine Communication

Use `host.docker.internal` instead of `localhost`:

```
mongodb://host.docker.internal:27017/mydb
```

> On Linux, add `--add-host=host.docker.internal:host-gateway`.

---

## 4. Container to Container — Basic Solution

Inspect one container's IP and use it from another (**fragile** — IPs change).

```bash
docker inspect <container> | grep IPAddress
```

---

## 5. Docker Networks — The Elegant Solution

Put containers in the **same network** — use container names as hostnames.

```bash
docker network create my-network
docker run -d --name mongodb --network my-network mongo
docker run -d --name my-app --network my-network -p 3000:3000 my-node-app
```

```
# Inside my-app, connect using container name:
mongodb://mongodb:27017/mydb
```

---

## 6. How Docker Resolves IP Addresses

Docker runs an **internal DNS server** that maps container names → IPs within the same network.

---

## 7. Docker Network Drivers

| Driver | Description | Use Case |
|--------|------------|----------|
| **bridge** (default) | Containers on same host communicate | Local development |
| **host** | Shares host network directly | Performance-sensitive |
| **overlay** | Cross-host communication | Swarm / multi-host |
| **none** | No networking | Isolated containers |

---

## 8. Network Commands

```bash
docker network create <name>
docker network ls
docker network rm <name>
docker network inspect <name>
docker network prune
```
