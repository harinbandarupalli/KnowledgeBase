# Section 9: Deploying Docker Containers

## 1. From Development to Production

| | Development | Production |
|--|-------------|------------|
| **Volumes** | Bind mounts (live code) | No bind mounts — code baked into image |
| **Build** | `docker compose up --build` | Build once, deploy image |
| **Compose** | Great for local setup | May use orchestrators (ECS, K8s) |
| **Multi-stage** | Optional | Recommended for smaller images |

---

## 2. Deployment Process & Providers

### General Steps
1. Build image → Push to registry (Docker Hub, ECR, etc.)
2. Set up remote host (AWS, Azure, DigitalOcean, etc.)
3. Pull image on remote → Run container

### Cloud Providers

| Provider | Service | Type |
|----------|---------|------|
| **AWS** | EC2 (manual), ECS (managed) | IaaS / Managed |
| **Azure** | Azure Container Instances | Managed |
| **Google Cloud** | Cloud Run, GKE | Managed |
| **DigitalOcean** | App Platform, Droplets | Managed / IaaS |

---

## 3. Deploying to AWS EC2 (Manual Approach)

### Getting Started
1. Create an **EC2 instance** (Amazon Linux / Ubuntu)
2. Configure **Security Group** — open ports (SSH: 22, HTTP: 80, app port)
3. Connect via SSH:

```bash
ssh -i my-key.pem ec2-user@<public-ip>
```

### Install Docker on EC2

```bash
# Amazon Linux
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
# Log out and back in

# Ubuntu
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo usermod -a -G docker ubuntu
```

### Push & Run

```bash
# On your machine — push to Docker Hub
docker build -t yourusername/my-app .
docker push yourusername/my-app

# On EC2 — pull and run
docker pull yourusername/my-app
docker run -d -p 80:3000 yourusername/my-app
```

### Updating the App

```bash
# On your machine
docker build -t yourusername/my-app .
docker push yourusername/my-app

# On EC2
docker pull yourusername/my-app
docker stop <container>
docker rm <container>
docker run -d -p 80:3000 yourusername/my-app
```

---

## 4. Disadvantages of Manual Deployment

- Must manage the server yourself (updates, security, scaling)
- Manual stops/starts for updates
- No auto-scaling, load balancing, or health checks
- SSH access management

---

## 5. Managed Services — AWS ECS

**ECS (Elastic Container Service)** handles container orchestration for you.

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Cluster** | Logical grouping of services |
| **Task Definition** | Blueprint for your container (image, ports, env vars) |
| **Service** | Runs and maintains desired count of tasks |
| **Fargate** | Serverless — no EC2 instances to manage |

### Benefits over EC2
- No server management
- Auto-scaling
- Load balancer integration
- Health checks and auto-restart
- Rolling deployments

---

## 6. Multi-Container Deployment on ECS

For apps with multiple containers (app + database):

1. Define **multiple containers** in a single Task Definition
2. Containers in the same task share `localhost`
3. Or use **separate services** with a shared VPC for isolation

---

## 7. Database Considerations

> ⚠️ Running databases in containers in production is **not always recommended**.

### Better Alternatives

| Option | Service |
|--------|---------|
| **MongoDB** | MongoDB Atlas (managed) |
| **MySQL/PostgreSQL** | AWS RDS, Azure DB, Cloud SQL |
| **Redis** | ElastiCache, Redis Cloud |

Benefits: automated backups, scaling, security patching, high availability.

---

## 8. Using Managed Database Services

```bash
# Instead of running mongo in a container:
# docker run -d mongo

# Use a managed connection string:
MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/mydb
```

Update your app's environment variables to point to the managed database.

---

## 9. Multi-Stage Builds for Production

Reduce image size by using **multi-stage builds**:

```dockerfile
# Stage 1: Build
FROM node:18-alpine AS build
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

```bash
docker build -t my-app:prod .
```

> Only the final stage ends up in the image — build tools and source are discarded.

---

## 10. Deployment Commands Summary

```bash
# Build and push to registry
docker build -t yourusername/app:latest .
docker push yourusername/app:latest

# On remote server
docker pull yourusername/app:latest
docker stop <old-container>
docker rm <old-container>
docker run -d -p 80:3000 --name app yourusername/app:latest

# Using Compose on remote
docker compose -f docker-compose.prod.yml up -d
```
