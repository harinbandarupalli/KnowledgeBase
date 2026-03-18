# Kubernetes Deployment (AWS EKS)

> **Duration**: 1 hr 38 min | **Lectures**: 16  
> **Goal**: Deploy Kubernetes workloads to production on AWS using EKS (Elastic Kubernetes Service), configure worker nodes, and set up persistent storage with AWS EFS.

---

## Table of Contents

1. [Deployment Options & Steps](#1-deployment-options--steps)
2. [AWS EKS vs AWS ECS](#2-aws-eks-vs-aws-ecs)
3. [Preparing the Starting Project](#3-preparing-the-starting-project)
4. [A Note on AWS EKS Pricing](#4-a-note-on-aws-eks-pricing)
5. [Diving Into AWS](#5-diving-into-aws)
6. [Creating & Configuring the Kubernetes Cluster with EKS](#6-creating--configuring-the-kubernetes-cluster-with-eks)
7. [Adding Worker Nodes](#7-adding-worker-nodes)
8. [Applying Our Kubernetes Config](#8-applying-our-kubernetes-config)
9. [Getting Started with Volumes on AWS](#9-getting-started-with-volumes-on-aws)
10. [Adding EFS as a Volume (CSI)](#10-adding-efs-as-a-volume-csi)
11. [Creating a Persistent Volume for EFS](#11-creating-a-persistent-volume-for-efs)
12. [Using the EFS Volume](#12-using-the-efs-volume)

---

## 1. Deployment Options & Steps

### Where Can You Deploy Kubernetes?

| Option | Description | Complexity | Cost |
|--------|-------------|-----------|------|
| **Custom (self-managed)** | Install K8s on your own servers | High | Variable |
| **Managed (cloud)** | EKS, GKE, AKS — cloud manages the control plane | Medium | Cloud pricing |
| **Local (development)** | Minikube, Docker Desktop, kind | Low | Free |

### Deployment Steps Overview

```
1. Build & Push Container Images
   └── Push to Docker Hub, ECR, GCR, or any registry

2. Create the Kubernetes Cluster
   └── EKS, GKE, AKS, or custom install

3. Configure Worker Nodes
   └── Add EC2 instances (EKS), VMs, or use managed node groups

4. Connect kubectl to the Cluster
   └── Update kubeconfig to point to the remote cluster

5. Apply Kubernetes Configuration
   └── kubectl apply -f <your-yaml-files>

6. Configure Storage (if needed)
   └── Set up PVs, PVCs, EFS/EBS volumes

7. Verify & Monitor
   └── Check pods, services, logs
```

---

## 2. AWS EKS vs AWS ECS

### Comparison

| Feature | EKS (Elastic Kubernetes Service) | ECS (Elastic Container Service) |
|---------|---------|---------|
| **Orchestrator** | Kubernetes (standard, open source) | AWS proprietary |
| **Portability** | Highly portable — same YAML works everywhere | AWS-only |
| **Learning curve** | Steeper (K8s concepts) | Simpler (AWS-native concepts) |
| **Ecosystem** | Massive K8s ecosystem, Helm charts, operators | AWS-specific tooling |
| **Pricing** | $0.10/hr per cluster + EC2/Fargate | EC2/Fargate only (no cluster fee) |
| **Config format** | Kubernetes YAML manifests | Task definitions (JSON/YAML) |
| **Service mesh** | Any (Istio, Linkerd, etc.) | AWS App Mesh |
| **Best for** | Multi-cloud, complex microservices, K8s expertise | Simple AWS-native deployments |

### When to Choose EKS

✅ You want cloud portability (avoid lock-in)  
✅ You already know Kubernetes  
✅ You need the rich K8s ecosystem (Helm, operators, CRDs)  
✅ You plan to run on multiple clouds  

### When to Choose ECS

✅ You're fully committed to AWS  
✅ You want simpler container orchestration  
✅ Cost sensitivity (no cluster management fee)  
✅ Smaller team, fewer microservices  

---

## 3. Preparing the Starting Project

### Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| **AWS CLI** | Interact with AWS from terminal | [aws.amazon.com/cli](https://aws.amazon.com/cli/) |
| **kubectl** | Interact with K8s cluster | Already installed from [Kubernetes in Action](./kubernetes-in-action.md) |
| **eksctl** (optional) | Simplified EKS cluster management | [eksctl.io](https://eksctl.io/) |
| **AWS Account** | Cloud resources | [aws.amazon.com](https://aws.amazon.com/) |

### Install & Configure AWS CLI

```bash
# Install AWS CLI (Windows)
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

# Configure credentials
aws configure
# AWS Access Key ID: <your-key>
# AWS Secret Access Key: <your-secret>
# Default region name: us-east-1
# Default output format: json

# Verify
aws sts get-caller-identity
```

### Push Images to a Registry

```bash
# Option A: Docker Hub
docker tag my-app:latest your-dockerhub-user/my-app:latest
docker push your-dockerhub-user/my-app:latest

# Option B: AWS ECR (Elastic Container Registry)
aws ecr create-repository --repository-name my-app

# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Tag and push
docker tag my-app:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
```

---

## 4. A Note on AWS EKS Pricing

### Cost Breakdown

| Component | Cost | Notes |
|-----------|------|-------|
| **EKS Control Plane** | **$0.10 / hour** (~$73/month) | Per cluster, always running |
| **EC2 Worker Nodes** | Varies by instance type | e.g., t3.medium = ~$30/month |
| **EBS Volumes** | ~$0.10/GB/month | For persistent storage |
| **EFS** | ~$0.30/GB/month | For shared filesystem |
| **Load Balancer (ELB)** | ~$0.025/hour + data | For external access |
| **Data Transfer** | Varies | Outbound data costs |

### Cost-Saving Tips

- **Use Spot Instances** for worker nodes (up to 90% savings)
- **Right-size instances** — don't over-provision
- **Delete clusters when not in use** (especially for learning!)
- **Use Fargate** instead of EC2 for sporadic workloads
- **Set billing alerts** in AWS to avoid surprises

> ⚠️ **Important**: Even an idle EKS cluster costs ~$73/month for the control plane alone. Always delete development clusters when done!

---

## 5. Diving Into AWS

### Key AWS Services for EKS

```
┌─────────────────────────────────────────────────────┐
│                    AWS Services                     │
│                                                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐            │
│  │   EKS   │  │   EC2   │  │   IAM   │            │
│  │ Control │  │ Worker  │  │ Roles & │            │
│  │  Plane  │  │  Nodes  │  │ Policies│            │
│  └─────────┘  └─────────┘  └─────────┘            │
│                                                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐            │
│  │   VPC   │  │  EFS /  │  │   ECR   │            │
│  │ Network │  │  EBS    │  │ Image   │            │
│  │         │  │ Storage │  │ Registry│            │
│  └─────────┘  └─────────┘  └─────────┘            │
│                                                     │
│  ┌─────────┐  ┌─────────┐                          │
│  │   ELB   │  │CloudForm│                          │
│  │  Load   │  │ation    │                          │
│  │Balancer │  │(infra)  │                          │
│  └─────────┘  └─────────┘                          │
└─────────────────────────────────────────────────────┘
```

### IAM Roles Needed

| Role | Purpose |
|------|---------|
| **EKS Cluster Role** | Allows EKS to manage AWS resources on your behalf |
| **EKS Node Role** | Allows EC2 instances (worker nodes) to call AWS APIs |
| **Your User/Role** | Must have EKS permissions to create and manage clusters |

---

## 6. Creating & Configuring the Kubernetes Cluster with EKS

### Option A: AWS Console (step-by-step)

1. **Go to EKS** in the AWS Console
2. **Create Cluster**:
   - Name: `kub-demo-cluster`
   - Kubernetes version: latest stable (e.g., 1.28)
   - Cluster Service Role: Create or select an IAM role with `AmazonEKSClusterPolicy`
3. **Networking**:
   - Select your VPC and subnets (at least 2 AZs for HA)
   - Security group: allow necessary ports
4. **Review & Create** (takes 10-15 minutes)

### Option B: eksctl (much simpler!)

```bash
# Install eksctl
choco install eksctl      # Windows
brew tap weaveworks/tap && brew install weaveworks/tap/eksctl  # macOS

# Create cluster with eksctl (all-in-one command)
eksctl create cluster \
  --name kub-demo-cluster \
  --region us-east-1 \
  --version 1.28 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed

# This creates: VPC, subnets, IAM roles, EKS cluster, AND node group!
# Takes about 15-20 minutes
```

### Connect kubectl to EKS

```bash
# Update kubeconfig to point to the new EKS cluster
aws eks update-kubeconfig --name kub-demo-cluster --region us-east-1

# Verify connection
kubectl get nodes
kubectl cluster-info
```

### What `update-kubeconfig` Does

It adds a new context to your `~/.kube/config` file:

```yaml
# ~/.kube/config (simplified)
clusters:
  - cluster:
      server: https://ABC123.gr7.us-east-1.eks.amazonaws.com
      certificate-authority-data: <base64-cert>
    name: kub-demo-cluster

contexts:
  - context:
      cluster: kub-demo-cluster
      user: aws-user
    name: kub-demo-cluster

current-context: kub-demo-cluster    # kubectl now talks to EKS!
```

### Switching Contexts (Minikube ↔ EKS)

```bash
# List all contexts
kubectl config get-contexts

# Switch to EKS
kubectl config use-context kub-demo-cluster

# Switch back to Minikube
kubectl config use-context minikube
```

---

## 7. Adding Worker Nodes

### What Are Worker Nodes on EKS?

On EKS, worker nodes are **EC2 instances** that run your Pods. You can add them via:

1. **Managed Node Groups** (recommended) — AWS handles provisioning and lifecycle
2. **Self-Managed Nodes** — You manage the EC2 instances yourself
3. **Fargate** — Serverless; AWS runs Pods without managing EC2 instances

### Adding a Managed Node Group (Console)

1. Go to your EKS cluster → **Compute** tab
2. Click **Add Node Group**
3. Configure:
   - Name: `standard-workers`
   - Node IAM Role: role with `AmazonEKSWorkerNodePolicy`, `AmazonEKS_CNI_Policy`, `AmazonEC2ContainerRegistryReadOnly`
   - Instance type: `t3.medium` (2 vCPU, 4 GB RAM)
   - Desired: 2 nodes, Min: 1, Max: 3

### Adding with eksctl

```bash
# Add a node group to an existing cluster
eksctl create nodegroup \
  --cluster kub-demo-cluster \
  --name standard-workers \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed
```

### Verify Nodes

```bash
kubectl get nodes

# Output:
# NAME                                       STATUS   ROLES    AGE   VERSION
# ip-192-168-1-100.ec2.internal              Ready    <none>   5m    v1.28.3
# ip-192-168-2-200.ec2.internal              Ready    <none>   5m    v1.28.3
```

---

## 8. Applying Our Kubernetes Config

### Deploy to EKS

The same YAML files you used locally with Minikube work on EKS!

```bash
# Make sure kubectl points to EKS
kubectl config current-context   # Should show EKS context

# Apply your configs
kubectl apply -f kubernetes/

# Or apply individual files
kubectl apply -f users-deployment.yaml
kubectl apply -f users-service.yaml
kubectl apply -f tasks-deployment.yaml
kubectl apply -f tasks-service.yaml
```

### LoadBalancer on AWS

When you create a `LoadBalancer` Service on EKS, AWS automatically provisions an **Elastic Load Balancer (ELB)**:

```bash
kubectl get services

# Output:
# NAME             TYPE           CLUSTER-IP    EXTERNAL-IP                           PORT(S)
# users-service    LoadBalancer   10.100.10.5   a1b2c3-1234.us-east-1.elb.amazonaws.com   8080:31234/TCP
```

The `EXTERNAL-IP` is a real, publicly accessible URL! No more `minikube service` workaround.

### Verify Everything

```bash
# Check all resources
kubectl get all

# Test the API
curl http://a1b2c3-1234.us-east-1.elb.amazonaws.com:8080/users

# Check logs
kubectl logs deployment/users-deployment
```

---

## 9. Getting Started with Volumes on AWS

### The Challenge

On Minikube we used `hostPath` volumes — that won't work on AWS because:

1. Pods might run on **different EC2 instances**
2. `hostPath` data is **node-specific** — if a Pod moves to another node, data is gone
3. EC2 instance storage is **ephemeral** (if the node is terminated)

### AWS Storage Options for Kubernetes

| Storage Type | AWS Service | Access Mode | Use Case |
|-------------|-------------|-------------|----------|
| **Block storage** | EBS (Elastic Block Store) | ReadWriteOnce (single node) | Databases, single-Pod storage |
| **File system** | EFS (Elastic File System) | ReadWriteMany (multi-node) | Shared storage across Pods |
| **Object storage** | S3 | N/A (not a volume type) | Backups, static assets |

### EBS vs EFS

| Feature | EBS | EFS |
|---------|-----|-----|
| **Type** | Block storage | Network file system (NFS) |
| **Access** | Single EC2 instance | Multiple EC2 instances |
| **Access modes** | ReadWriteOnce | ReadWriteMany |
| **Performance** | Higher IOPS | Lower latency at scale |
| **Cost** | ~$0.10/GB/month | ~$0.30/GB/month |
| **Use case** | Databases, single-Pod apps | Shared files, multi-Pod access |
| **Availability Zone** | Tied to one AZ | Spans multiple AZs |

---

## 10. Adding EFS as a Volume (CSI)

### Why EFS?

EFS supports **ReadWriteMany** — multiple Pods on different nodes can read and write simultaneously. This is critical for:
- Shared file uploads
- Shared configuration
- Multi-replica applications needing shared state

### Step 1: Install the EFS CSI Driver

```bash
# Add the EFS CSI driver to the cluster
kubectl apply -k "github.com/kubernetes-sigs/aws-efs-csi-driver/deploy/kubernetes/overlays/stable/?ref=release-1.7"

# Verify the driver is running
kubectl get pods -n kube-system -l app=efs-csi-controller
```

### Step 2: Create an EFS File System (AWS Console or CLI)

```bash
# Create a security group for EFS
aws ec2 create-security-group \
  --group-name efs-sg \
  --description "EFS Security Group" \
  --vpc-id <your-vpc-id>

# Allow NFS traffic (port 2049) from the cluster
aws ec2 authorize-security-group-ingress \
  --group-id <efs-sg-id> \
  --protocol tcp \
  --port 2049 \
  --source-group <cluster-security-group-id>

# Create EFS file system
aws efs create-file-system \
  --creation-token kub-demo-efs \
  --performance-mode generalPurpose \
  --region us-east-1

# Note the FileSystemId: fs-abc12345

# Create mount targets in each subnet
aws efs create-mount-target \
  --file-system-id fs-abc12345 \
  --subnet-id <subnet-1-id> \
  --security-groups <efs-sg-id>

aws efs create-mount-target \
  --file-system-id fs-abc12345 \
  --subnet-id <subnet-2-id> \
  --security-groups <efs-sg-id>
```

### Step 3: Create a StorageClass for EFS

```yaml
# efs-storageclass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: efs-sc
provisioner: efs.csi.aws.com
parameters:
  provisioningMode: efs-ap
  fileSystemId: fs-abc12345        # Your EFS file system ID
  directoryPerms: "700"
```

---

## 11. Creating a Persistent Volume for EFS

### PV & PVC for EFS

```yaml
# efs-pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: efs-pv
spec:
  capacity:
    storage: 5Gi                    # EFS is elastic, but K8s needs a number
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany                  # Multiple nodes can read/write!
  persistentVolumeReclaimPolicy: Retain
  storageClassName: efs-sc
  csi:
    driver: efs.csi.aws.com         # EFS CSI driver
    volumeHandle: fs-abc12345       # Your EFS file system ID

---
# efs-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: efs-pvc
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: efs-sc
  resources:
    requests:
      storage: 5Gi
```

### Apply

```bash
kubectl apply -f efs-storageclass.yaml
kubectl apply -f efs-pv.yaml
kubectl apply -f efs-pvc.yaml

# Check status
kubectl get sc
kubectl get pv
kubectl get pvc
```

---

## 12. Using the EFS Volume

### Deployment with EFS PVC

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: users-deployment
spec:
  replicas: 2                       # Multiple replicas all access the same EFS!
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
              value: "mongodb://mongodb-service:27017/users"
          volumeMounts:
            - name: efs-vol
              mountPath: /app/users-data     # Data directory in container
      volumes:
        - name: efs-vol
          persistentVolumeClaim:
            claimName: efs-pvc               # Reference the EFS PVC
```

### Verifying EFS Works Across Nodes

```bash
# Check which nodes the pods are running on
kubectl get pods -o wide

# Output:
# NAME                       READY   NODE
# users-deploy-abc12   1/1     ip-192-168-1-100.ec2.internal
# users-deploy-def34   1/1     ip-192-168-2-200.ec2.internal
# ^ Different nodes, same EFS volume!

# Write a file from Pod 1
kubectl exec users-deploy-abc12 -- sh -c "echo 'hello' > /app/users-data/test.txt"

# Read it from Pod 2
kubectl exec users-deploy-def34 -- cat /app/users-data/test.txt
# Output: hello  ← Shared storage works!
```

### Cleaning Up (Important for Cost!)

```bash
# Delete all K8s resources
kubectl delete -f kubernetes/

# Delete node group
eksctl delete nodegroup --cluster kub-demo-cluster --name standard-workers

# Delete EKS cluster
eksctl delete cluster --name kub-demo-cluster

# Delete EFS file system
aws efs delete-mount-target --mount-target-id <mt-id-1>
aws efs delete-mount-target --mount-target-id <mt-id-2>
aws efs delete-file-system --file-system-id fs-abc12345

# Verify everything is cleaned up
aws eks list-clusters
aws efs describe-file-systems
```

> ⚠️ **Always clean up AWS resources when done learning!** An idle EKS cluster costs ~$73/month just for the control plane.

---

## Summary — Key Takeaways

1. **AWS EKS** is a managed Kubernetes service — AWS runs the control plane, you manage worker nodes
2. **EKS vs ECS** — EKS is portable (standard K8s), ECS is AWS-proprietary but simpler
3. **eksctl** dramatically simplifies cluster creation (one command vs. many console steps)
4. **Same YAML configs work** from Minikube to EKS — that's the power of Kubernetes portability
5. **LoadBalancer Services** on AWS automatically get a real ELB with a public URL
6. **EBS** = block storage, single-node only (ReadWriteOnce)
7. **EFS** = network file system, multi-node (ReadWriteMany) — requires CSI driver
8. **Always clean up** development clusters to avoid unexpected costs

---

[← Kubernetes Networking](./kubernetes-networking.md) | [Back to Index](./README.md)
