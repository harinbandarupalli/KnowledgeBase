# Getting Started with Kubernetes

> **Duration**: 44 min | **Lectures**: 10 + Quiz  
> **Goal**: Understand *why* Kubernetes exists, *what* it is, and the high-level architecture.

---

## Table of Contents

1. [Problems with Manual Deployment](#1-problems-with-manual-deployment)
2. [Why Kubernetes?](#2-why-kubernetes)
3. [What Is Kubernetes Exactly?](#3-what-is-kubernetes-exactly)
4. [Architecture & Core Concepts](#4-architecture--core-concepts)
5. [Kubernetes Will NOT Manage Your Infrastructure](#5-kubernetes-will-not-manage-your-infrastructure)
6. [A Closer Look at Worker Nodes](#6-a-closer-look-at-worker-nodes)
7. [A Closer Look at the Master Node](#7-a-closer-look-at-the-master-node)
8. [Important Terms & Concepts](#8-important-terms--concepts)

---

## 1. Problems with Manual Deployment

### The Pain Points

When you deploy containers manually (even with Docker Compose on a remote host), several serious problems emerge:

| Problem | Description |
|---------|-------------|
| **Container crashes** | If a container goes down, no automatic restart or replacement occurs — you have to SSH in and fix it yourself. |
| **Traffic spikes** | A single container can't handle increased load; you need to manually spin up more instances. |
| **Traffic drops** | When load decreases, you're paying for idle containers — no automatic scale-down. |
| **Distributed hosts** | For high availability you need containers across multiple machines, but manually managing them is a nightmare. |
| **Deployment updates** | Rolling out a new version means manually stopping old containers and starting new ones, risking downtime. |

### What We Really Need

- **Automatic container health monitoring & restart** — if a container crashes, something should replace it immediately
- **Auto-scaling** — scale out when traffic rises, scale in when it drops
- **Load balancing** — distribute incoming traffic across container instances
- **Zero-downtime deployments** — roll out updates without user-facing interruptions

> 💡 These problems are the entire reason Kubernetes exists. It's a **container orchestrator** that automates all of the above.

---

## 2. Why Kubernetes?

### The Core Problem Statement

Using containers is excellent for development, but running them **in production** on remote machines introduces operational challenges:

1. **Containers might crash or go down** → needs to be detected and replaced automatically
2. **We might need more containers during peak** → needs auto-scaling
3. **Incoming traffic should be distributed** → needs load balancing
4. **Deploying updates should not cause downtime** → needs rolling updates

### Why Not Just Use Docker?

Docker is great at **building** and **running** single containers, but it doesn't provide:
- Cross-machine container orchestration
- Automatic restart/replacement of failed containers
- Horizontal scaling
- Service discovery and load balancing across containers

### Why Not AWS ECS / Manual Scripts?

- **Cloud-specific lock-in** — ECS works only on AWS
- **Custom scripts are fragile** — hard to maintain, error-prone, not battle-tested
- **Kubernetes is cloud-agnostic** — works on AWS, Azure, GCP, on-premise, or locally

### What Kubernetes IS

| Kubernetes IS | Kubernetes IS NOT |
|---|---|
| An open-source container orchestration system | A cloud service (though clouds offer managed K8s) |
| A framework for deploying, scaling, and managing containerized apps | A replacement for Docker — it _uses_ Docker (or containerd) |
| Cloud-agnostic and portable | A tool you must use — alternatives exist (Docker Swarm, Nomad) |
| Originally developed by Google, now maintained by CNCF | Simple to learn — it has a steep but worthwhile learning curve |

---

## 3. What Is Kubernetes Exactly?

### Official Definition

> **Kubernetes** (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications.

### Key Characteristics

- **Open source** — free, community-driven, vendor-neutral
- **Container orchestration** — manages the lifecycles of containers across a cluster of machines
- **Declarative configuration** — you describe the _desired state_ (e.g., "I want 3 replicas of this container"), and Kubernetes makes it happen
- **Self-healing** — automatically restarts failed containers, replaces them, and reschedules them on healthy nodes
- **Horizontal scaling** — add or remove container instances based on CPU/memory usage or custom metrics
- **Service discovery & load balancing** — automatically assigns DNS names or IPs and balances traffic
- **Automated rollouts & rollbacks** — gradually rolls out changes and can roll back to a previous version if something goes wrong
- **Secret & config management** — securely stores sensitive information (passwords, tokens)

### The Name

- "Kubernetes" is Greek for **helmsman** or **pilot** — the person who steers a ship
- Often abbreviated **K8s** (K + 8 characters + s)

---

## 4. Architecture & Core Concepts

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                   KUBERNETES CLUSTER                │
│                                                     │
│  ┌──────────────┐    ┌─────────────────────────┐   │
│  │ MASTER NODE  │    │      WORKER NODE(S)      │   │
│  │ (Control     │    │                          │   │
│  │  Plane)      │    │  ┌─────┐  ┌─────┐       │   │
│  │              │    │  │ Pod │  │ Pod │ ...    │   │
│  │ • API Server │◄──►│  │┌───┐│  │┌───┐│       │   │
│  │ • Scheduler  │    │  ││Con││  ││Con││       │   │
│  │ • Controller │    │  │└───┘│  │└───┘│       │   │
│  │   Manager    │    │  └─────┘  └─────┘       │   │
│  │ • etcd       │    │                          │   │
│  └──────────────┘    │  kubelet + kube-proxy    │   │
│                      └─────────────────────────┘   │
│                                                     │
│         kubectl (CLI) ──► API Server                │
└─────────────────────────────────────────────────────┘
```

### Components Overview

| Component | Role |
|-----------|------|
| **Cluster** | The full set of master + worker nodes |
| **Master Node** | Runs the control plane; makes scheduling decisions |
| **Worker Node** | Runs the actual application containers (inside Pods) |
| **Pod** | Smallest deployable unit — wraps one or more containers |
| **kubectl** | CLI tool to talk to the cluster's API Server |

---

## 5. Kubernetes Will NOT Manage Your Infrastructure

> ⚠️ **Critical understanding**: Kubernetes manages **containers and workloads**, not the underlying infrastructure.

### What You Must Provide

- **Cloud instances / VMs / bare-metal servers** — you provision them
- **A Kubernetes installation** on those machines (or use a managed service like EKS, AKS, GKE)
- **Container images** — you build and push them to a registry
- **Networking** — basic network between nodes must already work

### What Kubernetes Does For You

- Schedules containers onto available nodes
- Monitors health and restarts/replaces failed containers
- Scales workloads up and down
- Manages internal networking, DNS, and load balancing
- Handles rolling updates and rollbacks

### Managed Kubernetes Services

| Provider | Service | What it manages |
|----------|---------|-----------------|
| AWS | **EKS** (Elastic Kubernetes Service) | Master node + control plane |
| Google Cloud | **GKE** (Google Kubernetes Engine) | Master node + control plane |
| Microsoft Azure | **AKS** (Azure Kubernetes Service) | Master node + control plane |

> 💡 Even with managed services, **you** still manage worker nodes, container images, Pod definitions, and workload configurations.

---

## 6. A Closer Look at Worker Nodes

### What Is a Worker Node?

A **Worker Node** is a machine (physical or virtual) that runs your application containers. A cluster can have one or many worker nodes.

### Components on Every Worker Node

```
┌─────────────────────────────────────┐
│           WORKER NODE               │
│                                     │
│  ┌─────────┐  ┌─────────┐          │
│  │  Pod A   │  │  Pod B   │         │
│  │ ┌─────┐  │  │ ┌─────┐  │         │
│  │ │ Con │  │  │ │ Con │  │         │
│  │ └─────┘  │  │ └─────┘  │         │
│  │ Volume   │  │ Volume   │         │
│  └─────────┘  └─────────┘          │
│                                     │
│  ┌─────────────────────────┐        │
│  │        kubelet          │        │
│  │ (communicates with      │        │
│  │  master node)           │        │
│  └─────────────────────────┘        │
│                                     │
│  ┌─────────────────────────┐        │
│  │      kube-proxy         │        │
│  │ (manages network rules  │        │
│  │  & traffic)             │        │
│  └─────────────────────────┘        │
│                                     │
│  ┌─────────────────────────┐        │
│  │   Container Runtime     │        │
│  │ (Docker / containerd)   │        │
│  └─────────────────────────┘        │
└─────────────────────────────────────┘
```

| Component | Purpose |
|-----------|---------|
| **Pod** | Wraps one (or more) tightly coupled containers + shared volumes |
| **kubelet** | Agent that communicates with the Master Node's API Server; ensures containers are running |
| **kube-proxy** | Maintains network rules on the node so Pods can communicate within and outside the cluster |
| **Container Runtime** | Software responsible for running containers (Docker, containerd, CRI-O) |

### Pod Details

- A Pod is the **smallest deployable unit** in Kubernetes
- Usually holds **one main container** (though sidecar patterns use multiple)
- Containers in the same Pod share the same **network namespace** (localhost) and can share **volumes**
- Pods are **ephemeral** — they can be killed and replaced at any time
- You usually don't create Pods directly; instead, you create a **Deployment** which manages Pods

---

## 7. A Closer Look at the Master Node

### What Is the Master Node?

The **Master Node** (also called the **Control Plane**) is the brain of the cluster. It makes all scheduling decisions, monitors the cluster state, and responds to cluster events (e.g., a Pod crashing).

### Control Plane Components

```
┌──────────────────────────────────────┐
│           MASTER NODE                │
│           (Control Plane)            │
│                                      │
│  ┌────────────────────────────────┐  │
│  │         API Server             │  │
│  │  (central entry point for      │  │
│  │   all kubectl commands)        │  │
│  └──────────────┬─────────────────┘  │
│                 │                    │
│  ┌──────────────▼─────────────────┐  │
│  │         Scheduler              │  │
│  │  (decides which worker node    │  │
│  │   should run a new Pod)        │  │
│  └──────────────┬─────────────────┘  │
│                 │                    │
│  ┌──────────────▼─────────────────┐  │
│  │    Controller Manager          │  │
│  │  (monitors desired vs actual   │  │
│  │   state; takes corrective      │  │
│  │   action)                      │  │
│  └──────────────┬─────────────────┘  │
│                 │                    │
│  ┌──────────────▼─────────────────┐  │
│  │           etcd                 │  │
│  │  (distributed key-value store; │  │
│  │   stores all cluster state)    │  │
│  └────────────────────────────────┘  │
└──────────────────────────────────────┘
```

| Component | Purpose |
|-----------|---------|
| **API Server** | Front door for all REST commands (`kubectl` talks to this). Validates and processes API requests. |
| **Scheduler** | Watches for newly created Pods with no assigned node and selects a node for them to run on. |
| **Controller Manager** | Runs controller processes (Node Controller, Replication Controller, etc.) that watch the cluster state and make changes to move current state → desired state. |
| **etcd** | Consistent and highly-available key-value store used as K8s backing store for all cluster data. |

### How They Work Together (Example: Creating a Deployment)

1. You run `kubectl create deployment my-app --image=my-image`
2. **API Server** receives the request, validates it, stores the desired state in **etcd**
3. **Scheduler** notices a new Pod needs a node → picks a suitable Worker Node
4. **Controller Manager** monitors the desired state (1 replica of `my-app`) vs actual state
5. The chosen Worker Node's **kubelet** pulls the image and starts the container
6. If the container crashes, the **Controller Manager** detects the discrepancy and instructs a restart

---

## 8. Important Terms & Concepts

### Core Vocabulary

| Term | Definition |
|------|-----------|
| **Cluster** | A set of machines (nodes) that run containerized applications managed by Kubernetes |
| **Node** | A single machine in the cluster (can be master or worker) |
| **Master Node** | Node(s) running the control plane components |
| **Worker Node** | Node(s) running application workloads (Pods) |
| **Pod** | Smallest deployable unit; wraps one or more containers with shared storage/network |
| **Container** | A lightweight, standalone, executable package of software (Docker image instance) |
| **Deployment** | A Kubernetes object that manages a set of identical Pods, ensuring the desired number are running |
| **Service** | A stable network endpoint that exposes a set of Pods (provides load balancing and discovery) |
| **kubectl** | Command-line tool for interacting with the Kubernetes API Server |
| **kubelet** | Agent on each worker node that ensures containers are running in Pods |
| **kube-proxy** | Network proxy on each worker node that maintains network rules |
| **etcd** | Distributed key-value store holding all cluster state |
| **Namespace** | A way to divide cluster resources between multiple users or teams |
| **ReplicaSet** | Ensures a specified number of pod replicas are running at any given time (usually managed by Deployment) |

### Object Relationships

```
Deployment
  └── manages → ReplicaSet
                  └── manages → Pod(s)
                                  └── contains → Container(s)
                                                   └── runs → Your App
```

### Key Principles

1. **Desired State vs Actual State** — You declare what you want (desired state), and Kubernetes continuously works to match actual state to it.
2. **Self-Healing** — If a Pod dies, K8s replaces it. If a node dies, K8s reschedules Pods to other nodes.
3. **Declarative Configuration** — Instead of step-by-step commands, you provide YAML/JSON config files describing the end state.
4. **Immutable Infrastructure** — When you need to change a container, you build a new image and deploy it rather than modifying the running one.

---

## Quiz Review — Kubernetes Core Concepts

**Q1**: What is Kubernetes?  
**A**: An open-source container orchestration system for automating deployment, scaling, and management of containerized applications.

**Q2**: What is a Pod?  
**A**: The smallest deployable unit in Kubernetes. It wraps one or more containers with shared networking and storage.

**Q3**: Does Kubernetes replace Docker?  
**A**: No. Kubernetes uses a container runtime (like Docker/containerd) to run containers. K8s orchestrates them.

**Q4**: What is the role of the Master Node?  
**A**: It runs the control plane (API Server, Scheduler, Controller Manager, etcd) and makes all scheduling/management decisions.

**Q5**: What is the role of the Worker Node?  
**A**: It runs application workloads (Pods) and includes kubelet, kube-proxy, and a container runtime.

**Q6**: Does Kubernetes manage your cloud infrastructure?  
**A**: No. You must provision and manage the infrastructure (VMs, networking). Kubernetes manages the workloads on that infrastructure.

---

[← Back to Index](./README.md) | [Next: Kubernetes in Action →](./kubernetes-in-action.md)
