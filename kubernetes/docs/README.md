# 🚀 Kubernetes - Complete Reference Guide

A comprehensive knowledge base covering Kubernetes fundamentals, core concepts, data management, networking, and cloud deployment.

---

## 📚 Table of Contents

### Getting Started with Kubernetes
> **Duration**: 44 min | **Lectures**: 10 + Quiz

Covers the foundational "why" and "what" of Kubernetes: manual deployment pain points, Kubernetes architecture (master node, worker nodes), and essential terminology.

📄 [Getting Started Notes](./getting-started.md)

---

### Kubernetes in Action — Diving into the Core Concepts
> **Duration**: 2 hr 33 min | **Lectures**: 27

Hands-on deep dive: installation, `kubectl`, Deployments, Services, scaling, rollbacks, imperative vs. declarative approaches, labels & selectors, liveness probes, and configuration.

📄 [Kubernetes in Action Notes](./kubernetes-in-action.md)

---

### Managing Data & Volumes with Kubernetes
> **Duration**: 1 hr 45 min | **Lectures**: 18

State management in Kubernetes: ephemeral vs. persistent storage, volume types (`emptyDir`, `hostPath`, CSI), Persistent Volumes & Claims, environment variables, and ConfigMaps.

📄 [Managing Data & Volumes Notes](./managing-data-and-volumes.md)

---

### Kubernetes Networking
> **Duration**: 1 hr 47 min | **Lectures**: 17

Container-to-container and Pod-to-Pod communication: `localhost` for multi-container Pods, Kubernetes DNS service discovery, environment variables, reverse proxy pattern with Nginx, and deploying a containerized frontend.

📄 [Kubernetes Networking Notes](./kubernetes-networking.md)

---

### Kubernetes Deployment (AWS EKS)
> **Duration**: 1 hr 38 min | **Lectures**: 16

Production deployment on AWS: EKS vs ECS, cluster creation with `eksctl`, worker node configuration, connecting `kubectl`, EFS volumes with CSI driver, and cost management.

📄 [AWS EKS Deployment Notes](./aws-eks-deployment.md)

---

## 💻 Code Examples

All YAML configuration examples and scripts are in the [`../code/`](../code/) directory:

| Folder | Description |
|--------|-------------|
| [`deployments/`](../code/deployments/) | Deployment objects — imperative & declarative |
| [`services/`](../code/services/) | ClusterIP, NodePort, LoadBalancer Services |
| [`volumes/`](../code/volumes/) | emptyDir, hostPath, PV, PVC examples |
| [`configmaps/`](../code/configmaps/) | ConfigMaps & environment variables |
| [`probes/`](../code/probes/) | Liveness & readiness probe configs |
| [`networking/`](../code/networking/) | Multi-service app, Nginx reverse proxy |
| [`aws-eks/`](../code/aws-eks/) | EFS volume setup for AWS EKS |

---

## 🔑 Quick Reference — Key Commands

```bash
# Cluster info
kubectl cluster-info
kubectl get nodes

# Deployments
kubectl create deployment <name> --image=<image>
kubectl get deployments
kubectl rollout status deployment/<name>
kubectl rollout undo deployment/<name>

# Services
kubectl expose deployment <name> --type=LoadBalancer --port=8080
kubectl get services

# Scaling
kubectl scale deployment/<name> --replicas=3

# Declarative
kubectl apply -f <file.yaml>
kubectl delete -f <file.yaml>

# Volumes & Config
kubectl get pv
kubectl get pvc
kubectl get configmap

# Networking & DNS
kubectl get endpoints
kubectl exec <pod> -- nslookup <service-name>

# Context switching (Minikube ↔ Cloud)
kubectl config get-contexts
kubectl config use-context <context-name>

# AWS EKS
aws eks update-kubeconfig --name <cluster> --region <region>
eksctl create cluster --name <name> --region <region> --node-type t3.medium --nodes 2
eksctl delete cluster --name <name>
```
