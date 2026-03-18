# Kubernetes in Action — Diving into the Core Concepts

> **Duration**: 2 hr 33 min | **Lectures**: 27  
> **Goal**: Hands-on mastery of Kubernetes: setup, `kubectl`, Deployments, Services, scaling, rollbacks, declarative YAML, labels, selectors, liveness probes, and configuration.

---

## Table of Contents

1. [Kubernetes Does NOT Manage Your Infrastructure](#1-kubernetes-does-not-manage-your-infrastructure)
2. [Required Setup & Installation](#2-required-setup--installation)
3. [Understanding Kubernetes Objects (Resources)](#3-understanding-kubernetes-objects-resources)
4. [The Deployment Object](#4-the-deployment-object)
5. [A First Deployment — Imperative Approach](#5-a-first-deployment--imperative-approach)
6. [kubectl Behind The Scenes](#6-kubectl-behind-the-scenes)
7. [The Service Object](#7-the-service-object)
8. [Exposing a Deployment with a Service](#8-exposing-a-deployment-with-a-service)
9. [Restarting Containers](#9-restarting-containers)
10. [Scaling in Action](#10-scaling-in-action)
11. [Updating Deployments](#11-updating-deployments)
12. [Deployment Rollbacks & History](#12-deployment-rollbacks--history)
13. [Imperative vs Declarative Approach](#13-imperative-vs-declarative-approach)
14. [Creating a Deployment Config File (Declarative)](#14-creating-a-deployment-config-file-declarative)
15. [Adding Pod and Container Specs](#15-adding-pod-and-container-specs)
16. [Working with Labels & Selectors](#16-working-with-labels--selectors)
17. [Creating a Service Declaratively](#17-creating-a-service-declaratively)
18. [Updating & Deleting Resources](#18-updating--deleting-resources)
19. [Multiple vs Single Config Files](#19-multiple-vs-single-config-files)
20. [More on Labels & Selectors](#20-more-on-labels--selectors)
21. [Liveness Probes](#21-liveness-probes)
22. [Configuration Options Deep Dive](#22-configuration-options-deep-dive)

---

## 1. Kubernetes Does NOT Manage Your Infrastructure

> This is a **reinforcement** from the [Getting Started](./getting-started.md) section. It's repeated because it's the #1 misunderstanding.

### What YOU Must Set Up

```
You (Developer / DevOps)
├── Provision cloud instances (AWS EC2, GCP VMs, etc.)
├── Install Kubernetes on those instances
│   ├── Master Node(s) — control plane
│   └── Worker Node(s) — workload runners
├── Build and push container images to a registry
└── Write Kubernetes config (YAML / imperative commands)

Kubernetes (the software)
├── Schedules Pods onto Worker Nodes
├── Monitors and restarts failed Pods
├── Scales Pods up/down
├── Manages internal networking
└── Handles rolling updates & rollbacks
```

### Managed Kubernetes Simplifies This

With **EKS / GKE / AKS**, the cloud provider manages the Master Node for you. You still manage:
- Worker Node configuration & scaling
- Container images
- All Kubernetes workload definitions (Deployments, Services, etc.)

---

## 2. Required Setup & Installation

### What You Need

| Tool | Purpose | Install From |
|------|---------|-------------|
| **Docker Desktop** | Container runtime (includes K8s option) | [docker.com](https://www.docker.com/products/docker-desktop/) |
| **kubectl** | CLI to interact with K8s clusters | [kubernetes.io](https://kubernetes.io/docs/tasks/tools/) |
| **Minikube** | Local single-node K8s cluster for development | [minikube.sigs.k8s.io](https://minikube.sigs.k8s.io/docs/start/) |

### Windows Setup

```powershell
# Install Chocolatey (if not installed)
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install kubectl
choco install kubernetes-cli

# Install Minikube
choco install minikube

# Verify installations
kubectl version --client
minikube version
```

### Starting a Local Cluster

```bash
# Start Minikube (creates a single-node cluster)
minikube start --driver=docker

# Check cluster status
minikube status

# Check nodes
kubectl get nodes

# Open Minikube dashboard (optional)
minikube dashboard
```

### macOS Setup

```bash
# Using Homebrew
brew install kubectl
brew install minikube

# Start cluster
minikube start --driver=docker
```

---

## 3. Understanding Kubernetes Objects (Resources)

### What Are Kubernetes Objects?

Kubernetes Objects are **persistent entities in the Kubernetes system**. They represent the state of your cluster:

- What containerized applications are running (and on which nodes)
- The resources available to those applications
- Policies around how applications behave (restart, upgrades, fault-tolerance)

### Core Object Types

| Object | Purpose | Example |
|--------|---------|---------|
| **Pod** | Wraps container(s); smallest deployable unit | A running instance of your app |
| **Deployment** | Manages Pods, handles replicas & updates | "Run 3 copies of my web server" |
| **Service** | Stable network access to a set of Pods | "Expose my web server on port 80" |
| **ConfigMap** | Stores non-sensitive configuration data | Database host name, feature flags |
| **Secret** | Stores sensitive data (base64 encoded) | Passwords, API keys |
| **PersistentVolume** | Cluster-level storage resource | A disk provisioned in the cloud |
| **PersistentVolumeClaim** | A request for storage by a Pod | "Give me 10Gi of storage" |
| **Namespace** | Virtual sub-cluster for resource isolation | Separate dev/staging/prod |

### Object Spec & Status

Every Kubernetes object has two nested fields:

```yaml
apiVersion: apps/v1    # API group and version
kind: Deployment        # Object type
metadata:               # Name, namespace, labels
  name: my-app
spec:                   # DESIRED STATE — what you want
  replicas: 3
  ...
status:                 # ACTUAL STATE — what K8s reports (managed by K8s)
  availableReplicas: 3
  ...
```

- **spec** — You provide this. It's the desired state.
- **status** — Kubernetes maintains this. It's the current/actual state.
- Kubernetes constantly works to make `status` match `spec`.

---

## 4. The Deployment Object

### What Is a Deployment?

A **Deployment** is the most common way to run a stateless application on Kubernetes. It provides:

- **Pod management** — creates and manages Pods for you
- **Replicas** — ensures the desired number of Pod copies are running
- **Rolling updates** — gradually replaces old Pods with new ones
- **Rollbacks** — revert to a previous version if something goes wrong
- **Self-healing** — dead Pods are replaced automatically

### Deployment → ReplicaSet → Pod Hierarchy

```
Deployment
│
├── manages → ReplicaSet (v1)   ← current
│               └── Pod-1
│               └── Pod-2
│               └── Pod-3
│
└── manages → ReplicaSet (v2)   ← after an update
                └── Pod-4
                └── Pod-5
                └── Pod-6
```

- **Deployment** creates a **ReplicaSet** under the hood
- **ReplicaSet** ensures the correct number of **Pods** are running
- On update, Deployment creates a **new ReplicaSet** and scales down the old one
- Old ReplicaSets are kept (for rollback history)

### Why Not Create Pods Directly?

| Direct Pod Creation | Via Deployment |
|---|---|
| Pod dies → it's gone forever | Pod dies → Deployment creates a replacement |
| No scaling mechanism | Scale with `replicas` field or `kubectl scale` |
| No rolling updates | Automatic rolling updates on image change |
| No rollback | Full revision history with rollback support |

---

## 5. A First Deployment — Imperative Approach

### Imperative = Using `kubectl` Commands Directly

```bash
# Create a deployment imperatively
kubectl create deployment first-app --image=kub-first-app

# If using a local image (Minikube), point Docker to Minikube's daemon:
eval $(minikube docker-env)     # Linux/macOS
minikube docker-env | Invoke-Expression  # PowerShell

# Check deployment status
kubectl get deployments

# Check pods
kubectl get pods

# Check detailed info
kubectl describe deployment first-app
```

### Example Output

```
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
first-app   1/1     1            1           30s
```

### What Happens Behind the Scenes

1. `kubectl create deployment` sends a request to the **API Server**
2. API Server stores the Deployment object in **etcd**
3. The **Deployment Controller** (in Controller Manager) creates a **ReplicaSet**
4. The ReplicaSet Controller creates a **Pod**
5. The **Scheduler** assigns the Pod to a Worker Node
6. The Worker Node's **kubelet** pulls the image and starts the container

---

## 6. kubectl Behind The Scenes

### How kubectl Works

```
┌─────────┐         ┌────────────┐         ┌──────────┐
│ kubectl │ ──────► │ API Server │ ──────► │   etcd   │
│ (CLI)   │  HTTPS  │ (Master)   │  store  │ (state)  │
└─────────┘         └──────┬─────┘         └──────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ Scheduler│ │Controller│ │ kubelet  │
        │          │ │ Manager  │ │ (worker) │
        └──────────┘ └──────────┘ └──────────┘
```

### Key kubectl Commands Reference

```bash
# Get resources
kubectl get pods                      # List all pods
kubectl get deployments               # List deployments
kubectl get services                  # List services
kubectl get all                       # List everything

# Describe (detailed info)
kubectl describe pod <pod-name>
kubectl describe deployment <name>

# Logs
kubectl logs <pod-name>
kubectl logs <pod-name> -f            # Follow/stream logs

# Execute commands in a container
kubectl exec -it <pod-name> -- /bin/bash

# Delete resources
kubectl delete deployment <name>
kubectl delete service <name>
kubectl delete pod <name>             # Pod will be recreated by Deployment!
```

---

## 7. The Service Object

### Why Do We Need Services?

Pods are **ephemeral** — they get random IP addresses that change when Pods are recreated. A **Service** provides:

- A **stable IP address** (ClusterIP) that doesn't change
- A **stable DNS name** within the cluster
- **Load balancing** across multiple Pod replicas
- **External access** (depending on Service type)

### Service Types

| Type | Access | Use Case |
|------|--------|----------|
| **ClusterIP** (default) | Internal only — within the cluster | Backend services, databases |
| **NodePort** | External — via `<NodeIP>:<NodePort>` | Development, testing |
| **LoadBalancer** | External — via cloud load balancer | Production on cloud providers |
| **ExternalName** | Maps to an external DNS name | Referencing external services |

### How Services Find Pods — Labels & Selectors

```yaml
# Pod has a label
metadata:
  labels:
    app: my-web-app

# Service selects Pods with that label
spec:
  selector:
    app: my-web-app
```

The Service continuously watches for Pods matching its **selector** and routes traffic to them.

---

## 8. Exposing a Deployment with a Service

### Imperative Way

```bash
# Expose a deployment as a LoadBalancer service
kubectl expose deployment first-app --type=LoadBalancer --port=8080

# Check services
kubectl get services

# On Minikube, get the external URL
minikube service first-app
```

### Example Service Output

```
NAME        TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
first-app   LoadBalancer   10.99.207.51   <pending>     8080:30123/TCP   5s
kubernetes  ClusterIP      10.96.0.1      <none>        443/TCP          10m
```

> 💡 On Minikube, `EXTERNAL-IP` stays `<pending>` because there's no real cloud load balancer. Use `minikube service first-app` to get a tunneled URL.

### NodePort vs LoadBalancer

```
NodePort:
  Browser → <NodeIP>:30123 → Service → Pod

LoadBalancer:
  Browser → Cloud LB (external IP) → Service → Pod
```

---

## 9. Restarting Containers

### Kubernetes Handles Restarts Automatically

If a container inside a Pod crashes:

1. **kubelet** detects the container exited
2. kubelet **restarts the container** (not the Pod — the Pod stays, just the container restarts)
3. K8s uses an exponential backoff (10s, 20s, 40s, …, up to 5 min) if it keeps crashing

### Restart Policies

| Policy | Behavior |
|--------|----------|
| `Always` (default) | Always restart the container when it exits |
| `OnFailure` | Only restart if the container exits with a non-zero exit code |
| `Never` | Never restart the container |

### Testing Self-Healing

```bash
# Crash a container (e.g., your app has a /crash endpoint)
curl <service-url>/crash

# Watch the pod — it will restart automatically
kubectl get pods -w

# You'll see RESTARTS count increase:
# NAME                         READY   STATUS    RESTARTS   AGE
# first-app-6d5bc4f7c4-abc12   1/1     Running   1          5m
```

---

## 10. Scaling in Action

### Horizontal Scaling

```bash
# Scale up to 3 replicas
kubectl scale deployment/first-app --replicas=3

# Check pods — should see 3
kubectl get pods

# Scale back down to 1
kubectl scale deployment/first-app --replicas=1
```

### What Happens When You Scale

```
Before (1 replica):        After (3 replicas):
┌─────────┐               ┌─────────┐  ┌─────────┐  ┌─────────┐
│  Pod-1  │               │  Pod-1  │  │  Pod-2  │  │  Pod-3  │
└─────────┘               └─────────┘  └─────────┘  └─────────┘
     ▲                         ▲            ▲            ▲
     │                         └────────────┼────────────┘
  Service                            Service (load balances)
```

### Load Balancing

The **Service** automatically distributes traffic across all healthy Pod replicas. If one Pod crashes, traffic is routed to the remaining Pods while K8s replaces the failed one.

---

## 11. Updating Deployments

### Rolling Updates

When you update a Deployment's image, K8s performs a **rolling update**:

```bash
# Update the image
kubectl set image deployment/first-app kub-first-app=your-registry/kub-first-app:v2

# Watch the rollout
kubectl rollout status deployment/first-app
```

### Rolling Update Process

```
Step 1: Create new Pod with v2 image
  v1: Pod-1 ✓  Pod-2 ✓  Pod-3 ✓
  v2: Pod-4 (starting)

Step 2: New Pod ready → terminate one old Pod
  v1: Pod-1 ✓  Pod-2 ✓  [Pod-3 terminating]
  v2: Pod-4 ✓

Step 3: Repeat until all Pods are v2
  v1: [all terminated]
  v2: Pod-4 ✓  Pod-5 ✓  Pod-6 ✓
```

### Update Strategies

| Strategy | Behavior |
|----------|----------|
| **RollingUpdate** (default) | Gradually replaces old Pods; zero downtime |
| **Recreate** | Kills all old Pods first, then creates new ones; brief downtime |

### RollingUpdate Parameters

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # Max Pods above desired count during update
      maxUnavailable: 0   # Max Pods that can be unavailable during update
```

---

## 12. Deployment Rollbacks & History

### View Rollout History

```bash
# See revision history
kubectl rollout history deployment/first-app

# See details of a specific revision
kubectl rollout history deployment/first-app --revision=2
```

### Rollback to Previous Revision

```bash
# Rollback to the previous version
kubectl rollout undo deployment/first-app

# Rollback to a specific revision
kubectl rollout undo deployment/first-app --to-revision=1

# Check rollout status
kubectl rollout status deployment/first-app
```

### How Rollbacks Work

- Old **ReplicaSets** are preserved (not deleted after an update)
- A rollback simply scales up the old ReplicaSet and scales down the current one
- This is why rollbacks are nearly **instant** — the old configuration and image reference still exist

```bash
# You can see old ReplicaSets
kubectl get replicasets

# Example output:
# NAME                    DESIRED   CURRENT   READY   AGE
# first-app-6d5bc4f7c4    3         3         3       2m    ← current
# first-app-7a8b9c0d1e    0         0         0       10m   ← previous (kept for rollback)
```

---

## 13. Imperative vs Declarative Approach

### Two Ways to Work with Kubernetes

| Aspect | Imperative | Declarative |
|--------|-----------|-------------|
| **How** | Execute specific commands (`create`, `scale`, `expose`) | Define YAML config files and `kubectl apply` them |
| **Analogy** | Giving step-by-step instructions | Describing the end goal |
| **Example** | `kubectl create deployment...` | `kubectl apply -f deployment.yaml` |
| **Pros** | Quick, simple for one-off tasks | Reproducible, version-controlled, auditable |
| **Cons** | Not reproducible, hard to track changes | More verbose, need to learn YAML syntax |
| **Best for** | Testing, quick experiments, learning | Production, CI/CD pipelines, team collaboration |

### Imperative Example

```bash
kubectl create deployment my-app --image=my-image
kubectl expose deployment my-app --type=LoadBalancer --port=8080
kubectl scale deployment my-app --replicas=3
```

### Declarative Example

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app
          image: my-image
          ports:
            - containerPort: 8080
```

```bash
kubectl apply -f deployment.yaml
```

> 💡 **Best Practice**: Use **imperative** for quick testing and learning. Use **declarative** for everything in production.

---

## 14. Creating a Deployment Config File (Declarative)

### Basic Deployment YAML Structure

```yaml
apiVersion: apps/v1          # API version for Deployment
kind: Deployment              # Resource type
metadata:
  name: second-app-deployment # Name of the Deployment
  labels:
    app: second-app           # Labels for the Deployment itself
spec:
  replicas: 1                 # Number of Pod replicas
  selector:
    matchLabels:
      app: second-app         # How Deployment finds its Pods
  template:                   # Pod template
    metadata:
      labels:
        app: second-app       # Labels on the Pods (must match selector)
    spec:
      containers:
        - name: second-node   # Container name
          image: academind/kub-first-app:2  # Container image
```

### Key Fields Explained

| Field | Description |
|-------|-------------|
| `apiVersion` | API group and version. Deployments use `apps/v1` |
| `kind` | The type of Kubernetes object |
| `metadata.name` | Unique name for this resource within the namespace |
| `metadata.labels` | Key-value pairs for identification and selection |
| `spec.replicas` | Desired number of identical Pods |
| `spec.selector.matchLabels` | How the Deployment identifies Pods it manages |
| `spec.template` | Blueprint for creating Pods |
| `spec.template.metadata.labels` | Labels on created Pods — **must match selector** |
| `spec.template.spec.containers` | List of containers to run in each Pod |

### Applying the Configuration

```bash
# Create or update resources defined in the file
kubectl apply -f deployment.yaml

# Verify
kubectl get deployments
kubectl get pods
```

---

## 15. Adding Pod and Container Specs

### Container Specification Options

```yaml
spec:
  containers:
    - name: my-container
      image: my-image:latest
      
      # Port the container listens on
      ports:
        - containerPort: 8080
          protocol: TCP
      
      # Resource limits and requests
      resources:
        requests:
          memory: "128Mi"    # Minimum memory
          cpu: "250m"        # Minimum CPU (250 millicores = 0.25 cores)
        limits:
          memory: "256Mi"    # Maximum memory
          cpu: "500m"        # Maximum CPU
      
      # Environment variables
      env:
        - name: DB_HOST
          value: "mongodb-service"
        - name: DB_PORT
          value: "27017"
      
      # Volume mounts
      volumeMounts:
        - name: my-volume
          mountPath: /app/data
```

### Multi-Container Pods (Sidecar Pattern)

```yaml
spec:
  containers:
    - name: main-app
      image: my-app:latest
      ports:
        - containerPort: 8080

    - name: log-agent
      image: log-collector:latest
      volumeMounts:
        - name: shared-logs
          mountPath: /var/log

  volumes:
    - name: shared-logs
      emptyDir: {}
```

> 💡 All containers in a Pod share the same network (localhost) and can share volumes.

---

## 16. Working with Labels & Selectors

### What Are Labels?

Labels are **key-value pairs** attached to objects (Pods, Deployments, Services, etc.). They do not affect runtime behavior but are used for **organization** and **selection**.

```yaml
metadata:
  labels:
    app: users-api
    environment: production
    team: backend
    version: v2.1
```

### What Are Selectors?

Selectors allow you to **filter and select** objects based on their labels.

### Selector Types

| Type | Syntax | Example |
|------|--------|---------|
| **Equality-based** | `=`, `==`, `!=` | `app=my-app`, `env!=production` |
| **Set-based** | `in`, `notin`, `exists` | `env in (prod, staging)` |

### Using Selectors in kubectl

```bash
# Get pods with a specific label
kubectl get pods -l app=my-app

# Get pods with multiple labels (AND logic)
kubectl get pods -l app=my-app,env=production

# Get pods NOT in production
kubectl get pods -l 'env notin (production)'

# Delete pods by label
kubectl delete pods -l app=my-app
```

### matchLabels vs matchExpressions

```yaml
# Simple — matchLabels (equality-based only)
selector:
  matchLabels:
    app: my-app

# Advanced — matchExpressions (set-based)
selector:
  matchExpressions:
    - key: app
      operator: In
      values:
        - my-app
        - my-app-canary
    - key: env
      operator: NotIn
      values:
        - test
```

---

## 17. Creating a Service Declaratively

### Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  selector:
    app: second-app       # Matches Pods with this label
  ports:
    - protocol: TCP
      port: 80             # Port the Service listens on
      targetPort: 8080     # Port the container listens on
  type: LoadBalancer        # Service type
```

### Applying

```bash
kubectl apply -f service.yaml
kubectl get services
```

### Port Mapping Explained

```
External Request
       │
       ▼
   Service (port: 80)
       │
       ▼
   Pod Container (targetPort: 8080)
```

| Port Field | Meaning |
|-----------|---------|
| `port` | The port the Service is available on (what clients connect to) |
| `targetPort` | The port the container is actually listening on |
| `nodePort` | (NodePort type only) Port on the node itself (30000-32767 range) |

---

## 18. Updating & Deleting Resources

### Updating with `kubectl apply`

```bash
# Edit the YAML file (change image, replicas, etc.)
# Then re-apply
kubectl apply -f deployment.yaml

# Kubernetes compares the new spec with the existing one
# and makes only the necessary changes
```

### Deleting Resources

```bash
# Delete by file (recommended — clean and precise)
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

# Delete by name
kubectl delete deployment second-app-deployment
kubectl delete service backend-service

# Delete everything with a label
kubectl delete all -l app=second-app

# Delete everything in a namespace (DANGEROUS!)
kubectl delete all --all
```

> ⚠️ `kubectl delete -f <file>` is the cleanest way — it deletes exactly what the file defines. Use it in production.

---

## 19. Multiple vs Single Config Files

### Separate Files (Recommended for Large Projects)

```
k8s/
├── deployment.yaml
├── service.yaml
├── configmap.yaml
└── pvc.yaml
```

```bash
# Apply all files in a directory
kubectl apply -f k8s/

# Delete all resources defined in the directory
kubectl delete -f k8s/
```

### Single File (Good for Small Projects)

Multiple objects in one file, separated by `---`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  selector:
    app: second-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: second-app-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: second-app
  template:
    metadata:
      labels:
        app: second-app
    spec:
      containers:
        - name: second-node
          image: academind/kub-first-app:2
          ports:
            - containerPort: 8080
```

> 💡 **Best Practice**: Put the **Service before the Deployment** in a combined file. This ensures the Service exists before Pods try to use it.

---

## 20. More on Labels & Selectors

### Using Labels for Organization

Labels are incredibly powerful for managing a large number of resources:

```yaml
# Group resources by application
app: frontend
app: backend
app: database

# Group by environment
environment: dev
environment: staging
environment: production

# Group by release
release: stable
release: canary

# Group by team
team: platform
team: payments
```

### Filtering with kubectl

```bash
# Show labels on pods
kubectl get pods --show-labels

# Filter by multiple criteria
kubectl get pods -l 'app=backend,environment=production'

# Set-based filtering
kubectl get pods -l 'environment in (dev, staging)'
kubectl get pods -l 'team!=payments'

# Check if a label exists (regardless of value)
kubectl get pods -l 'canary'
```

### Annotations vs Labels

| Feature | Labels | Annotations |
|---------|--------|-------------|
| Purpose | Identification & selection | Non-identifying metadata |
| Used by selectors | ✅ Yes | ❌ No |
| Character limit | 63 chars (value) | 256 KB total |
| Examples | `app=my-app` | `build-date=2024-01-15`, `git-commit=abc123` |

---

## 21. Liveness Probes

### What Are Liveness Probes?

A **Liveness Probe** tells Kubernetes whether a container is still **alive and healthy**. If the probe fails, K8s **restarts the container**.

> ⚠️ Without a liveness probe, K8s only knows if the container _process_ crashed. It can't detect if the app is hung, deadlocked, or returning errors.

### Types of Liveness Probes

| Type | How It Works | Best For |
|------|-------------|----------|
| **HTTP GET** | Sends an HTTP request; success = 2xx/3xx status | Web servers, REST APIs |
| **TCP Socket** | Tries to open a TCP connection | Databases, non-HTTP services |
| **Exec** | Runs a command inside the container; success = exit code 0 | Custom health checks, CLI apps |

### HTTP GET Probe Example

```yaml
spec:
  containers:
    - name: my-app
      image: my-image
      ports:
        - containerPort: 8080
      livenessProbe:
        httpGet:
          path: /healthz       # Endpoint to check
          port: 8080
        initialDelaySeconds: 15  # Wait before first check
        periodSeconds: 10        # Check every 10 seconds
        failureThreshold: 3      # Restart after 3 consecutive failures
        timeoutSeconds: 1        # Timeout for each probe
```

### TCP Socket Probe Example

```yaml
livenessProbe:
  tcpSocket:
    port: 3306               # Try to connect on MySQL port
  initialDelaySeconds: 15
  periodSeconds: 20
```

### Exec Probe Example

```yaml
livenessProbe:
  exec:
    command:
      - cat
      - /tmp/healthy          # If file exists, container is healthy
  initialDelaySeconds: 5
  periodSeconds: 5
```

### Probe Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `initialDelaySeconds` | 0 | Seconds to wait after container start before probing |
| `periodSeconds` | 10 | How often to probe |
| `timeoutSeconds` | 1 | Seconds after which the probe times out |
| `successThreshold` | 1 | Consecutive successes needed after a failure |
| `failureThreshold` | 3 | Consecutive failures before restarting |

### Readiness Probes (Bonus)

A **Readiness Probe** tells Kubernetes if a container is ready to **accept traffic**. Unlike liveness probes, failing a readiness probe doesn't restart the container — it just removes it from the Service's endpoints.

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

---

## 22. Configuration Options Deep Dive

### Container Image Pull Policy

```yaml
spec:
  containers:
    - name: my-app
      image: my-image:latest
      imagePullPolicy: Always   # Always pull (good for :latest)
```

| Policy | Behavior |
|--------|----------|
| `Always` | Always pull the image, even if it exists locally |
| `IfNotPresent` | Pull only if the image doesn't exist locally |
| `Never` | Never pull; image must already exist locally |

> 💡 If you use `:latest` tag, K8s defaults to `Always`. For specific tags, it defaults to `IfNotPresent`.

### Resource Requests and Limits

```yaml
resources:
  requests:            # Minimum guaranteed resources
    memory: "64Mi"
    cpu: "250m"
  limits:              # Maximum allowed resources
    memory: "128Mi"
    cpu: "500m"
```

| Concept | Behavior |
|---------|----------|
| **Request** | Scheduler uses this to decide which node has capacity |
| **Limit** | Container is killed (OOMKilled) or throttled if exceeded |
| **No request** | Scheduled anywhere, might be evicted under pressure |
| **No limit** | Can consume all available node resources |

### Restart Policy

```yaml
spec:
  restartPolicy: Always    # Always | OnFailure | Never
```

### DNS Policy

```yaml
spec:
  dnsPolicy: ClusterFirst  # Default — use cluster DNS
```

---

## Summary — Key Takeaways

1. **Kubernetes objects** represent the desired state of your cluster
2. **Deployments** manage Pods and provide scaling, updates, and rollbacks
3. **Services** provide stable networking for ephemeral Pods
4. **Imperative** = quick commands; **Declarative** = YAML files (preferred for production)
5. **Labels & Selectors** are the glue that connects Services to Pods
6. **Liveness Probes** let K8s know if your app is truly healthy
7. **Rolling Updates** ensure zero-downtime deployments
8. **Rollbacks** are instant because old ReplicaSets are retained

---

[← Getting Started](./getting-started.md) | [Back to Index](./README.md) | [Next: Managing Data & Volumes →](./managing-data-and-volumes.md)
