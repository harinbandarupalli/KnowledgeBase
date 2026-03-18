# Kubernetes Networking

> **Duration**: 1 hr 47 min | **Lectures**: 17  
> **Goal**: Master container-to-container, Pod-to-Pod, and Pod-to-Service communication patterns inside and across Kubernetes Pods, including DNS-based service discovery and frontend deployment with reverse proxies.

---

## Table of Contents

1. [Starting Project & Our Goal](#1-starting-project--our-goal)
2. [Creating a Deployment](#2-creating-a-deployment)
3. [Another Look at Services](#3-another-look-at-services)
4. [Multiple Containers in One Pod](#4-multiple-containers-in-one-pod)
5. [Pod-Internal Communication](#5-pod-internal-communication)
6. [Creating Multiple Deployments](#6-creating-multiple-deployments)
7. [Pod-to-Pod Communication with IP Addresses & Environment Variables](#7-pod-to-pod-communication-with-ip-addresses--environment-variables)
8. [Using DNS for Pod-to-Pod Communication](#8-using-dns-for-pod-to-pod-communication)
9. [Which Approach Is Best?](#9-which-approach-is-best)
10. [Adding a Containerized Frontend](#10-adding-a-containerized-frontend)
11. [Deploying the Frontend with Kubernetes](#11-deploying-the-frontend-with-kubernetes)
12. [Using a Reverse Proxy for the Frontend](#12-using-a-reverse-proxy-for-the-frontend)

---

## 1. Starting Project & Our Goal

### The Scenario

We have a multi-service application:

```
┌──────────────────────────────────────────────────┐
│                  Our Application                 │
│                                                  │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐ │
│  │  Frontend   │  │  Users API │  │  Tasks API │ │
│  │  (React)    │  │  (Node.js) │  │  (Node.js) │ │
│  │             │  │            │  │            │ │
│  │  Port 3000  │  │  Port 8080 │  │  Port 8000 │ │
│  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘ │
│        │               │               │        │
│        └───────────────┼───────────────┘        │
│                        │                         │
│                   ┌────▼────┐                    │
│                   │ MongoDB │                    │
│                   └─────────┘                    │
└──────────────────────────────────────────────────┘
```

### Our Goal

- Make containers within the same Pod communicate via `localhost`
- Make Pods in different Deployments communicate with each other
- Deploy a frontend that talks to backend APIs
- Understand Kubernetes DNS and service discovery

---

## 2. Creating a Deployment

### Starting with the Users API

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: users
  template:
    metadata:
      labels:
        app: users
    spec:
      containers:
        - name: users-api
          image: academind/kub-demo-users:latest
          ports:
            - containerPort: 8080
          env:
            - name: MONGODB_CONNECTION_URI
              value: "mongodb://localhost:27017/users"
```

> 💡 Notice `localhost:27017` — this only works if MongoDB is in the **same Pod** as the users-api container.

---

## 3. Another Look at Services

### Service Recap & Deeper Dive

Services provide **stable networking** for ephemeral Pods. Let's understand the networking layers:

```
┌─────────────────────────────────────────────┐
│              Kubernetes Networking           │
│                                             │
│  Layer 1: Container-to-Container            │
│  ├── Same Pod → localhost                   │
│  └── Shared network namespace               │
│                                             │
│  Layer 2: Pod-to-Pod                        │
│  ├── Via Service (recommended)              │
│  ├── Via Pod IP (not recommended)           │
│  └── Via DNS (service-name.namespace)       │
│                                             │
│  Layer 3: External-to-Pod                   │
│  ├── NodePort Service                       │
│  ├── LoadBalancer Service                   │
│  └── Ingress Controller                     │
└─────────────────────────────────────────────┘
```

### Service Endpoints

A Service automatically maintains a list of **Endpoints** — the IP addresses of healthy Pods matching its selector:

```bash
# View endpoints for a service
kubectl get endpoints users-service

# Output:
# NAME            ENDPOINTS           AGE
# users-service   172.17.0.4:8080     5m
```

### ClusterIP — The Internal Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: users-service
spec:
  type: ClusterIP          # Only accessible inside the cluster
  selector:
    app: users
  ports:
    - port: 8080
      targetPort: 8080
```

> 💡 **ClusterIP** is the default type and is perfect for internal microservice communication — other Pods can reach it, but external traffic cannot.

---

## 4. Multiple Containers in One Pod

### Why Put Multiple Containers in the Same Pod?

When containers are **tightly coupled** and need to:
- Share the same **network namespace** (communicate via `localhost`)
- Share the same **volumes**
- Be scheduled on the **same node**
- Scale **together** (not independently)

### Example: Users API + MongoDB in One Pod

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: users
  template:
    metadata:
      labels:
        app: users
    spec:
      containers:
        # Container 1: Users API
        - name: users-api
          image: academind/kub-demo-users:latest
          ports:
            - containerPort: 8080
          env:
            - name: MONGODB_CONNECTION_URI
              value: "mongodb://localhost:27017/users"  # localhost!

        # Container 2: MongoDB
        - name: users-db
          image: mongo:latest
          ports:
            - containerPort: 27017
```

### When NOT to Use Multi-Container Pods

| ❌ Don't combine | ✅ Do combine |
|---|---|
| Independently scalable services | Sidecar logging/monitoring agents |
| Loosely coupled microservices | Init containers for setup tasks |
| Services with different lifecycles | Proxy/adapter containers |
| Frontend + Backend | Main app + config reloader |

---

## 5. Pod-Internal Communication

### How It Works

Containers within the **same Pod** share a network namespace. They communicate via **`localhost`**:

```
┌──────────────────────────────────────────┐
│                   POD                    │
│                                          │
│  ┌──────────────┐  ┌──────────────┐     │
│  │  users-api   │  │   MongoDB    │     │
│  │  Port 8080   │  │  Port 27017  │     │
│  │              │  │              │     │
│  │ connects to: │  │              │     │
│  │ localhost:   │──►              │     │
│  │ 27017        │  │              │     │
│  └──────────────┘  └──────────────┘     │
│                                          │
│  Shared Network Namespace (localhost)    │
│  Shared Volumes (if configured)         │
└──────────────────────────────────────────┘
```

### Key Rules

1. All containers in a Pod share `localhost`
2. Containers must use **different ports** (port conflicts = crash)
3. No Service needed for intra-Pod communication
4. Containers can also share volumes defined at the Pod level

### Code Example (Node.js)

```javascript
// In users-api container:
// MongoDB is in the same Pod, so we use localhost
const mongoUri = 'mongodb://localhost:27017/users';
mongoose.connect(mongoUri);

// The API listens on port 8080
app.listen(8080);
```

---

## 6. Creating Multiple Deployments

### Separating Concerns — Better Architecture

Instead of cramming everything into one Pod, create **separate Deployments** for each service:

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   Deployment 1   │    │   Deployment 2   │    │   Deployment 3   │
│   users-api      │    │   tasks-api      │    │   mongodb        │
│                  │    │                  │    │                  │
│  ┌────────────┐  │    │  ┌────────────┐  │    │  ┌────────────┐  │
│  │  Pod       │  │    │  │  Pod       │  │    │  │  Pod       │  │
│  │  users-api │  │    │  │  tasks-api │  │    │  │  MongoDB   │  │
│  └────────────┘  │    │  └────────────┘  │    │  └────────────┘  │
└──────────────────┘    └──────────────────┘    └──────────────────┘
        │                       │                       │
        ▼                       ▼                       ▼
  ┌────────────┐         ┌────────────┐          ┌────────────┐
  │  Service   │         │  Service   │          │  Service   │
  │  users-svc │         │  tasks-svc │          │  mongodb-svc│
  │  ClusterIP │         │  ClusterIP │          │  ClusterIP │
  └────────────┘         └────────────┘          └────────────┘
```

### Why Separate Deployments?

| Benefit | Description |
|---------|-------------|
| **Independent scaling** | Scale the API without scaling the database |
| **Independent updates** | Update one service without affecting others |
| **Fault isolation** | If one Pod crashes, others stay running |
| **Resource control** | Set different CPU/memory limits per service |
| **Team ownership** | Different teams can own different Deployments |

---

## 7. Pod-to-Pod Communication with IP Addresses & Environment Variables

### Option 1: Using Pod IP (NOT Recommended)

```bash
# Get Pod IP
kubectl get pods -o wide

# Output:
# NAME                      READY   STATUS    IP            NODE
# mongodb-abc123            1/1     Running   172.17.0.4    minikube
```

You could hardcode `172.17.0.4`... but Pod IPs change when Pods restart! ❌

### Option 2: Using Service IP (Better)

When you create a Service, Kubernetes injects environment variables into every Pod:

```bash
# For a service named "mongodb-service", K8s auto-creates:
MONGODB_SERVICE_SERVICE_HOST=10.96.100.50
MONGODB_SERVICE_SERVICE_PORT=27017
```

### Using the Auto-Generated Env Vars in Code

```javascript
// Node.js — using the auto-injected environment variables
const mongoHost = process.env.MONGODB_SERVICE_SERVICE_HOST;
const mongoPort = process.env.MONGODB_SERVICE_SERVICE_PORT;
const mongoUri = `mongodb://${mongoHost}:${mongoPort}/users`;
```

### Environment Variable Naming Convention

The Service name is transformed:
1. Converted to UPPERCASE
2. Dashes (`-`) become underscores (`_`)
3. Suffixed with `_SERVICE_HOST` and `_SERVICE_PORT`

| Service Name | Host Env Var | Port Env Var |
|-------------|-------------|-------------|
| `mongodb-service` | `MONGODB_SERVICE_SERVICE_HOST` | `MONGODB_SERVICE_SERVICE_PORT` |
| `users-service` | `USERS_SERVICE_SERVICE_HOST` | `USERS_SERVICE_SERVICE_PORT` |
| `backend` | `BACKEND_SERVICE_HOST` | `BACKEND_SERVICE_PORT` |

### Caveat

> ⚠️ Services must exist **before** the Pods that reference them — environment variables are only injected at Pod creation time.

---

## 8. Using DNS for Pod-to-Pod Communication

### The Best Approach: Kubernetes DNS

Kubernetes runs an internal DNS server (**CoreDNS**). Every Service gets a DNS name automatically:

```
<service-name>.<namespace>.svc.cluster.local
```

### DNS Resolution Examples

| Service Name | Namespace | Full DNS Name | Short Name (same namespace) |
|-------------|-----------|---------------|---------------------------|
| `mongodb-service` | `default` | `mongodb-service.default.svc.cluster.local` | `mongodb-service` |
| `users-service` | `default` | `users-service.default.svc.cluster.local` | `users-service` |
| `auth-service` | `prod` | `auth-service.prod.svc.cluster.local` | `auth-service.prod` |

### Using DNS in Code

```javascript
// Simply use the service name as the hostname!
// (Works within the same namespace)
const mongoUri = 'mongodb://mongodb-service:27017/users';

// For cross-namespace access, include the namespace:
const authUrl = 'http://auth-service.prod:8080/verify';
```

### Why DNS Is Best

| Env Vars | DNS |
|----------|-----|
| Injected only at Pod start | Resolved at connection time |
| Service must exist before Pod | Order doesn't matter |
| Name format is clunky | Clean, readable names |
| No cross-namespace support | Full cross-namespace support |

### DNS in Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: users
  template:
    metadata:
      labels:
        app: users
    spec:
      containers:
        - name: users-api
          image: academind/kub-demo-users:latest
          ports:
            - containerPort: 8080
          env:
            - name: MONGODB_CONNECTION_URI
              value: "mongodb://mongodb-service:27017/users"  # DNS name!
            - name: AUTH_API_URL
              value: "http://auth-service:3000"               # DNS name!
```

---

## 9. Which Approach Is Best?

### Communication Decision Matrix

```
Need to reach another container?
│
├── Same Pod?
│   └── YES → Use localhost:<port>
│
├── Different Pod, same namespace?
│   └── Use DNS: <service-name>:<port>
│
├── Different Pod, different namespace?
│   └── Use DNS: <service-name>.<namespace>:<port>
│
└── External service?
    └── Use full URL / ExternalName Service
```

### Summary Table

| Method | Example | Recommended? |
|--------|---------|-------------|
| **localhost** (same Pod) | `localhost:27017` | ✅ For tightly coupled containers |
| **Pod IP** | `172.17.0.4:27017` | ❌ IPs change on restart |
| **Service env vars** | `$MONGODB_SERVICE_SERVICE_HOST` | ⚠️ Works but order-dependent |
| **DNS** (same namespace) | `mongodb-service:27017` | ✅ **Best approach** |
| **DNS** (cross-namespace) | `mongodb-service.prod:27017` | ✅ **Best approach** |
| **FQDN** | `mongodb-service.prod.svc.cluster.local` | ✅ Most explicit |

---

## 10. Adding a Containerized Frontend

### The Frontend Challenge

Frontend apps (React, Angular, Vue) run in the **browser**, not in the cluster. So:

```
┌──────────────────────────────────────────────────────┐
│                KUBERNETES CLUSTER                    │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ Frontend │  │ Users    │  │ Tasks    │          │
│  │ (Nginx)  │  │ API      │  │ API      │          │
│  │ serves   │  │          │  │          │          │
│  │ static   │  │          │  │          │          │
│  │ files    │  │          │  │          │          │
│  └────┬─────┘  └──────────┘  └──────────┘          │
│       │                                              │
└───────┼──────────────────────────────────────────────┘
        │
        ▼ (downloads JS/HTML/CSS)
┌──────────────────┐
│   USER'S BROWSER │
│                  │        ❌ Can't use K8s DNS!
│   React App      │────►  "users-service:8080"
│   runs HERE      │        doesn't resolve in
│                  │        the browser!
└──────────────────┘
```

### The Problem

- Kubernetes DNS (`users-service:8080`) works **inside the cluster**
- The React app runs in the **browser** (outside the cluster)
- The browser can't resolve Kubernetes service names!

### Solutions

1. **Expose APIs with LoadBalancer/NodePort** — Frontend uses external URLs
2. **Use a reverse proxy** (Nginx) — Frontend and API calls go through the same host ✅

---

## 11. Deploying the Frontend with Kubernetes

### Frontend Dockerfile

```dockerfile
# Build stage
FROM node:14-alpine as build
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# Production stage — serve with Nginx
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Frontend Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: frontend
          image: academind/kub-demo-frontend:latest
          ports:
            - containerPort: 80
```

### Frontend Service (LoadBalancer for external access)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
spec:
  type: LoadBalancer
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 80
```

---

## 12. Using a Reverse Proxy for the Frontend

### Why a Reverse Proxy?

Instead of exposing each API service externally, route all traffic through **Nginx** in the frontend container:

```
Browser Request: /api/users
       │
       ▼
┌──────────────────────────┐
│  Frontend Pod (Nginx)    │
│                          │
│  / → serve React app     │
│  /api/users → proxy to   │──► users-service:8080 (internal DNS)
│  /api/tasks → proxy to   │──► tasks-service:8000 (internal DNS)
│                          │
└──────────────────────────┘
```

### Nginx Configuration (nginx.conf)

```nginx
server {
    listen 80;

    # Serve the React frontend
    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;    # SPA fallback
    }

    # Reverse proxy to Users API
    location /api/users {
        proxy_pass http://users-service:8080/users;    # K8s DNS!
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Reverse proxy to Tasks API
    location /api/tasks {
        proxy_pass http://tasks-service:8000/tasks;    # K8s DNS!
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Benefits of the Reverse Proxy Pattern

| Benefit | Description |
|---------|-------------|
| **Single entry point** | Only one Service needs external exposure |
| **K8s DNS works** | Nginx runs inside the cluster and can resolve service names |
| **CORS eliminated** | Frontend and API share the same origin |
| **Security** | Backend APIs stay internal (ClusterIP) |
| **SSL termination** | Terminate HTTPS at the proxy level |

### Updated Frontend Code

```javascript
// Before (with external API URLs — fragile):
fetch('http://35.180.100.50:8080/users')

// After (with reverse proxy — clean):
fetch('/api/users')
```

### Complete Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     KUBERNETES CLUSTER                      │
│                                                             │
│  ┌──────────────────┐                                       │
│  │  Frontend Pod    │   ┌────────────────┐                  │
│  │  (Nginx)         │   │  Users API Pod │                  │
│  │                  │──►│  (ClusterIP)   │                  │
│  │  LoadBalancer    │   └────────────────┘                  │
│  │  Service ◄───────│── External Traffic                    │
│  │                  │   ┌────────────────┐                  │
│  │  Serves React +  │   │  Tasks API Pod │                  │
│  │  proxies /api/*  │──►│  (ClusterIP)   │                  │
│  └──────────────────┘   └────────┬───────┘                  │
│                                  │                          │
│                         ┌────────▼───────┐                  │
│                         │  MongoDB Pod   │                  │
│                         │  (ClusterIP)   │                  │
│                         └────────────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Summary — Key Takeaways

1. **Pod-internal communication** uses `localhost` — containers in the same Pod share a network namespace
2. **Pod-to-Pod communication** should use **Kubernetes DNS**: `<service-name>:<port>`
3. **DNS is superior** to environment variables — no ordering dependency, cleaner syntax, cross-namespace capable
4. **Separate Deployments** per microservice allows independent scaling, updates, and fault isolation
5. **Frontend apps** run in the browser, so they can't use K8s DNS directly
6. A **reverse proxy** (Nginx) solves the frontend-to-API communication problem elegantly
7. **ClusterIP** Services keep backends internal; only the frontend needs external exposure

---

[← Managing Data & Volumes](./managing-data-and-volumes.md) | [Back to Index](./README.md) | [Next: AWS EKS Deployment →](./aws-eks-deployment.md)
