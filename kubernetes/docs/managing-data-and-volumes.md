# Managing Data & Volumes with Kubernetes

> **Duration**: 1 hr 45 min | **Lectures**: 18  
> **Goal**: Understand how to persist and share data in Kubernetes using Volumes, Persistent Volumes, PVCs, environment variables, and ConfigMaps.

---

## Table of Contents

1. [Kubernetes & Volumes — More Than Docker Volumes](#1-kubernetes--volumes--more-than-docker-volumes)
2. [Kubernetes Volumes: Theory & Docker Comparison](#2-kubernetes-volumes-theory--docker-comparison)
3. [Creating a New Deployment & Service](#3-creating-a-new-deployment--service)
4. [Getting Started with Kubernetes Volumes](#4-getting-started-with-kubernetes-volumes)
5. [Volume Type: emptyDir](#5-volume-type-emptydir)
6. [Volume Type: hostPath](#6-volume-type-hostpath)
7. [Volume Type: CSI](#7-volume-type-csi)
8. [From Volumes to Persistent Volumes](#8-from-volumes-to-persistent-volumes)
9. [Defining a Persistent Volume](#9-defining-a-persistent-volume)
10. [Creating a Persistent Volume Claim](#10-creating-a-persistent-volume-claim)
11. [Using a Claim in a Pod](#11-using-a-claim-in-a-pod)
12. [Volumes vs Persistent Volumes](#12-volumes-vs-persistent-volumes)
13. [Using Environment Variables](#13-using-environment-variables)
14. [Environment Variables & ConfigMaps](#14-environment-variables--configmaps)

---

## 1. Kubernetes & Volumes — More Than Docker Volumes

### The Data Problem in Kubernetes

Containers are **ephemeral** by design. When a container restarts, all data written inside the container's filesystem is **lost**. This is a problem for:

- Application logs
- User-uploaded files
- Database storage
- Session data
- Temporary computation results

### Docker Volumes vs Kubernetes Volumes

| Feature | Docker Volumes | Kubernetes Volumes |
|---------|---------------|-------------------|
| **Scope** | Single host | Cluster-wide (with the right type) |
| **Lifetime** | Persists until manually deleted | Tied to Pod lifetime (regular volumes) or cluster (persistent volumes) |
| **Types** | Named volumes, bind mounts, tmpfs | emptyDir, hostPath, CSI, NFS, cloud-specific, PV/PVC, and many more |
| **Cross-node** | ❌ Not natively | ✅ With network/cloud storage types |
| **Configuration** | `docker run -v` or `docker-compose.yaml` | Pod spec YAML |

### Key Insight

> 💡 Kubernetes volumes are **much more powerful and flexible** than Docker volumes. They support dozens of storage backends and can survive Pod restarts (and even Pod deletion, with Persistent Volumes).

---

## 2. Kubernetes Volumes: Theory & Docker Comparison

### Volume Lifecycle

```
Regular Volume (e.g., emptyDir):
┌─────────────────────────────┐
│ Lifetime = Pod Lifetime     │
│                             │
│  Pod Created → Volume created  │
│  Container restarts → Data survives  │
│  Pod deleted → Volume DELETED  │
└─────────────────────────────┘

Persistent Volume (PV/PVC):
┌─────────────────────────────┐
│ Lifetime = Independent      │
│                             │
│  PV created → exists in cluster  │
│  Pod uses PVC → gets access │
│  Pod deleted → PV SURVIVES  │
│  PV must be manually deleted  │
└─────────────────────────────┘
```

### Volume Types Overview

| Type | Scope | Survives Pod Deletion? | Use Case |
|------|-------|----------------------|----------|
| `emptyDir` | Pod-level | ❌ No | Temp files, cache, inter-container sharing |
| `hostPath` | Node-level | ✅ Yes (on same node) | Dev/testing, node-level logs |
| `CSI` | Cluster/Cloud | ✅ Yes | Production cloud storage |
| `nfs` | Network | ✅ Yes | Shared network storage |
| `persistentVolumeClaim` | Cluster | ✅ Yes | Production persistent storage |
| `configMap` | Cluster | N/A | Configuration files |
| `secret` | Cluster | N/A | Sensitive configuration |

---

## 3. Creating a New Deployment & Service

### Sample Deployment for Volume Examples

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: story-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: story
  template:
    metadata:
      labels:
        app: story
    spec:
      containers:
        - name: story
          image: academind/kub-data-demo:1
          ports:
            - containerPort: 3000
```

### Sample Service

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: story-service
spec:
  selector:
    app: story
  type: LoadBalancer
  ports:
    - protocol: TCP
      port: 80
      targetPort: 3000
```

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

## 4. Getting Started with Kubernetes Volumes

### How Volumes Work

1. **Define the volume** in the Pod spec (under `spec.volumes`)
2. **Mount the volume** into a container (under `spec.containers[].volumeMounts`)

```yaml
spec:
  containers:
    - name: my-app
      image: my-image
      volumeMounts:                    # Step 2: Mount
        - mountPath: /app/data         # Where in the container
          name: data-volume            # Which volume to mount
  volumes:                             # Step 1: Define
    - name: data-volume                # Volume name (referenced above)
      emptyDir: {}                     # Volume type and config
```

### Key Concepts

- A volume is defined at the **Pod level** (not the container level)
- Multiple containers in the same Pod can mount the **same volume**
- The `mountPath` is the directory path **inside the container**
- The `name` links the mount to the volume definition

---

## 5. Volume Type: emptyDir

### What Is emptyDir?

An `emptyDir` volume is created when a Pod is assigned to a node. It starts as an **empty directory**. All containers in the Pod can read and write to it.

### Characteristics

| Property | Value |
|----------|-------|
| **Created** | When Pod is assigned to a node |
| **Initial state** | Empty |
| **Survives container restart** | ✅ Yes |
| **Survives Pod deletion** | ❌ No |
| **Shared across containers** | ✅ Yes (within same Pod) |
| **Storage medium** | Node's disk (default) or RAM (`medium: Memory`) |

### Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: story-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: story
  template:
    metadata:
      labels:
        app: story
    spec:
      containers:
        - name: story
          image: academind/kub-data-demo:1
          ports:
            - containerPort: 3000
          volumeMounts:
            - mountPath: /app/story
              name: story-volume
      volumes:
        - name: story-volume
          emptyDir: {}
```

### When to Use emptyDir

✅ Temporary scratch space  
✅ Cache that can be regenerated  
✅ Sharing files between containers in the same Pod  
✅ Sorting/processing large datasets  

❌ Data that must survive Pod deletion  
❌ Data shared across multiple Pods  

### RAM-backed emptyDir

```yaml
volumes:
  - name: cache-volume
    emptyDir:
      medium: Memory       # Use RAM instead of disk
      sizeLimit: 256Mi     # Limit the size
```

> ⚠️ RAM-backed volumes count against the container's memory limit and are lost on node restart.

---

## 6. Volume Type: hostPath

### What Is hostPath?

A `hostPath` volume mounts a file or directory from the **host node's filesystem** into the Pod.

### Characteristics

| Property | Value |
|----------|-------|
| **Source** | File/directory on the node's filesystem |
| **Survives container restart** | ✅ Yes |
| **Survives Pod deletion** | ✅ Yes (data stays on the node) |
| **Survives Pod rescheduling** | ❌ No (different node = different data) |
| **Multi-node safe** | ❌ No |

### Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: story-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: story
  template:
    metadata:
      labels:
        app: story
    spec:
      containers:
        - name: story
          image: academind/kub-data-demo:1
          ports:
            - containerPort: 3000
          volumeMounts:
            - mountPath: /app/story
              name: story-volume
      volumes:
        - name: story-volume
          hostPath:
            path: /data               # Path on the HOST node
            type: DirectoryOrCreate   # Create if doesn't exist
```

### hostPath Types

| Type | Behavior |
|------|----------|
| `""` (empty) | No checks before mounting |
| `DirectoryOrCreate` | Create directory if it doesn't exist |
| `Directory` | Directory must already exist |
| `FileOrCreate` | Create file if it doesn't exist |
| `File` | File must already exist |

### When to Use hostPath

✅ Single-node clusters (like Minikube) for development  
✅ Accessing node-level files (e.g., `/var/log`)  
✅ Running DaemonSets that need host access  

❌ Multi-node production clusters (data is node-specific!)  
❌ Storing application data that must be available everywhere  

> ⚠️ **Security Warning**: `hostPath` can expose the entire node filesystem. Use with extreme caution in production.

---

## 7. Volume Type: CSI

### What Is CSI?

**Container Storage Interface (CSI)** is a standard API that allows Kubernetes to interact with **any storage provider** through a plugin.

### Why CSI Matters

Before CSI, every storage provider had custom code baked into Kubernetes core. CSI solved this by:

- **Decoupling** storage driver code from Kubernetes
- Allowing storage vendors to **develop and deploy** their own drivers
- Making it easy to add **new storage backends** without changing K8s

### Architecture

```
┌───────────────┐
│  Kubernetes   │
│   (kubelet)   │
└──────┬────────┘
       │  CSI Interface (gRPC)
       ▼
┌───────────────┐
│  CSI Driver   │ ← Provided by storage vendor
│  (plugin)     │
└──────┬────────┘
       │
       ▼
┌───────────────┐
│  Storage      │ ← AWS EBS, GCP PD, Azure Disk,
│  Backend      │   Ceph, NetApp, etc.
└───────────────┘
```

### Popular CSI Drivers

| Provider | CSI Driver |
|----------|-----------|
| AWS | [aws-ebs-csi-driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) |
| GCP | [gcp-compute-persistent-disk-csi-driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) |
| Azure | [azuredisk-csi-driver](https://github.com/kubernetes-sigs/azuredisk-csi-driver) |
| DigitalOcean | [csi-digitalocean](https://github.com/digitalocean/csi-digitalocean) |
| NFS | [csi-driver-nfs](https://github.com/kubernetes-csi/csi-driver-nfs) |

### Example CSI Volume Usage

```yaml
volumes:
  - name: my-csi-volume
    csi:
      driver: ebs.csi.aws.com       # CSI driver name
      volumeAttributes:
        size: "10Gi"
```

> 💡 In practice, you typically use CSI through **StorageClasses** and **PersistentVolumeClaims** rather than directly.

---

## 8. From Volumes to Persistent Volumes

### The Problem with Regular Volumes

| Issue | Description |
|-------|-------------|
| **Lifecycle coupling** | Regular volumes are tied to Pod lifecycle |
| **Configuration in Pod spec** | Volume config is mixed with application config |
| **No reuse** | Can't easily share volume config across Pods |
| **Admin vs Dev separation** | Developers shouldn't need to know storage infrastructure details |

### The Solution: PV + PVC Architecture

```
Cluster Admin:                     Developer:
┌───────────────────┐             ┌──────────────────┐
│ PersistentVolume  │             │ PersistentVolume  │
│ (PV)              │ ◄── binds ──│ Claim (PVC)       │
│                   │             │                    │
│ • Storage type    │             │ • Requested size   │
│ • Capacity        │             │ • Access mode      │
│ • Access modes    │             │                    │
│ • Reclaim policy  │             └─────────┬──────────┘
└───────────────────┘                       │
                                            │ used by
                                            ▼
                                   ┌──────────────────┐
                                   │      Pod         │
                                   │  volumeMounts:   │
                                   │   - name: data   │
                                   │     mountPath:   │
                                   │     /app/data    │
                                   └──────────────────┘
```

### Key Benefits

1. **Separation of concerns** — Admins provision storage, developers request it
2. **Lifecycle independence** — PVs survive Pod and even PVC deletion
3. **Reuse** — Multiple Pods can reference the same PVC
4. **Abstraction** — Developers don't need to know underlying storage details

---

## 9. Defining a Persistent Volume

### PersistentVolume (PV) YAML

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: host-pv
spec:
  capacity:
    storage: 1Gi                    # Total storage capacity
  volumeMode: Filesystem            # Filesystem or Block
  storageClassName: standard        # Storage class (for matching with PVCs)
  accessModes:
    - ReadWriteOnce                 # Access mode
  hostPath:                         # Underlying storage (hostPath for dev)
    path: /data
    type: DirectoryOrCreate
```

### Access Modes

| Mode | Abbreviation | Description |
|------|-------------|-------------|
| `ReadWriteOnce` | RWO | Can be mounted as read-write by a **single node** |
| `ReadOnlyMany` | ROX | Can be mounted as read-only by **many nodes** |
| `ReadWriteMany` | RWX | Can be mounted as read-write by **many nodes** |
| `ReadWriteOncePod` | RWOP | Can be mounted as read-write by a **single Pod** (K8s 1.22+) |

> ⚠️ Not all storage backends support all access modes. `hostPath` only supports `ReadWriteOnce`.

### Reclaim Policies

| Policy | Behavior |
|--------|----------|
| `Retain` | PV is kept after PVC is deleted. Data preserved. Manual cleanup required. |
| `Delete` | PV and underlying storage are deleted when PVC is deleted. |
| `Recycle` | (Deprecated) Basic scrub (`rm -rf /volume/*`) and makes PV available again. |

```yaml
spec:
  persistentVolumeReclaimPolicy: Retain  # or Delete
```

### Applying

```bash
kubectl apply -f host-pv.yaml
kubectl get pv
```

---

## 10. Creating a Persistent Volume Claim

### PersistentVolumeClaim (PVC) YAML

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: host-pvc
spec:
  volumeName: host-pv              # Specific PV name (optional)
  accessModes:
    - ReadWriteOnce
  storageClassName: standard       # Must match PV's storageClassName
  resources:
    requests:
      storage: 1Gi                 # Requested storage size
```

### How PVC-to-PV Binding Works

```
PVC Request:                    Available PVs:
┌──────────────────┐           ┌──────────────────┐
│ accessModes: RWO │           │ PV-1: 5Gi, RWO   │ ← Too big? Still matches!
│ storage: 1Gi     │ ──bind──► │ PV-2: 1Gi, RWO   │ ← Perfect match
│ class: standard  │           │ PV-3: 1Gi, RWX   │ ← Wrong access mode
└──────────────────┘           │ PV-4: 1Gi, fast   │ ← Wrong class
                               └──────────────────┘
```

Kubernetes matches PVCs to PVs based on:
1. **storageClassName** must match
2. **accessModes** must be compatible
3. **capacity** must be >= requested size
4. **volumeName** (if specified) must match exactly

### Applying

```bash
kubectl apply -f host-pvc.yaml
kubectl get pvc

# Output:
# NAME       STATUS   VOLUME    CAPACITY   ACCESS MODES   STORAGECLASS   AGE
# host-pvc   Bound    host-pv   1Gi        RWO            standard       5s
```

---

## 11. Using a Claim in a Pod

### Deployment Using PVC

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: story-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: story
  template:
    metadata:
      labels:
        app: story
    spec:
      containers:
        - name: story
          image: academind/kub-data-demo:2
          ports:
            - containerPort: 3000
          volumeMounts:
            - mountPath: /app/story        # Where to mount in container
              name: story-volume            # References volume below
      volumes:
        - name: story-volume
          persistentVolumeClaim:
            claimName: host-pvc            # References the PVC created earlier
```

### Full Workflow

```bash
# 1. Create the PV (admin)
kubectl apply -f host-pv.yaml

# 2. Create the PVC (developer)
kubectl apply -f host-pvc.yaml

# 3. Deploy the app using the PVC
kubectl apply -f deployment.yaml

# 4. Create the service
kubectl apply -f service.yaml

# Verify everything
kubectl get pv
kubectl get pvc
kubectl get deployments
kubectl get pods
kubectl get services
```

---

## 12. Volumes vs Persistent Volumes

### Comparison Table

| Feature | Regular Volume | Persistent Volume (PV/PVC) |
|---------|---------------|---------------------------|
| **Defined in** | Pod spec | Separate YAML resources |
| **Lifetime** | Tied to Pod | Independent of Pods |
| **Survives Pod deletion** | ❌ (emptyDir) / Depends (hostPath) | ✅ Yes |
| **Reusable across Pods** | ❌ No (must redefine) | ✅ Yes (via PVC) |
| **Admin/Dev separation** | ❌ Mixed | ✅ Admin creates PV, Dev creates PVC |
| **Dynamic provisioning** | ❌ | ✅ Via StorageClasses |
| **Best for** | Ephemeral data, caches | Databases, file storage, stateful apps |

### When to Use What

```
Decision Tree:

Does the data need to survive Pod deletion?
├── NO → Use emptyDir
└── YES
    ├── Is this a single-node dev cluster?
    │   └── YES → hostPath is acceptable
    └── Is this production / multi-node?
        └── YES → Use PersistentVolume + PVC
            ├── Cloud? → Use CSI driver (EBS, GCP PD, etc.)
            ├── On-prem? → Use NFS, Ceph, or other network storage
            └── Want auto-provisioning? → Use StorageClass + Dynamic PVC
```

### Dynamic Provisioning with StorageClasses

Instead of manually creating PVs, you can use a **StorageClass** to automatically provision storage:

```yaml
# storageclass.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
```

```yaml
# PVC that triggers dynamic provisioning
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: dynamic-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast-storage   # References the StorageClass
  resources:
    requests:
      storage: 10Gi
# No volumeName → K8s automatically creates a PV via the StorageClass provisioner!
```

---

## 13. Using Environment Variables

### Hardcoded Environment Variables

```yaml
spec:
  containers:
    - name: my-app
      image: my-image
      env:
        - name: STORY_FOLDER
          value: "story"
        - name: DB_HOST
          value: "mongodb-service"
        - name: DB_PORT
          value: "27017"
        - name: NODE_ENV
          value: "production"
```

### Accessing in Code

```javascript
// Node.js
const storyFolder = process.env.STORY_FOLDER;
const dbHost = process.env.DB_HOST;
```

```python
# Python
import os
story_folder = os.environ.get('STORY_FOLDER')
db_host = os.environ.get('DB_HOST')
```

### Environment Variables from Other Sources

```yaml
env:
  # From a ConfigMap key
  - name: DB_HOST
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: database-host

  # From a Secret key
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: app-secrets
        key: db-password

  # From Pod field (downward API)
  - name: POD_NAME
    valueFrom:
      fieldRef:
        fieldPath: metadata.name

  # From container resource
  - name: MEMORY_LIMIT
    valueFrom:
      resourceFieldRef:
        containerName: my-app
        resource: limits.memory
```

---

## 14. Environment Variables & ConfigMaps

### What Is a ConfigMap?

A **ConfigMap** is a Kubernetes object that stores **non-sensitive configuration data** as key-value pairs. It decouples configuration from container images, making applications more portable.

### Creating a ConfigMap

#### Declarative (YAML)

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # Simple key-value pairs
  database-host: "mongodb-service"
  database-port: "27017"
  story-folder: "story"
  log-level: "info"
  
  # Multi-line file content
  app-config.json: |
    {
      "port": 3000,
      "debug": false,
      "features": {
        "darkMode": true
      }
    }
```

#### Imperative

```bash
# From literal values
kubectl create configmap app-config \
  --from-literal=database-host=mongodb-service \
  --from-literal=database-port=27017

# From a file
kubectl create configmap app-config --from-file=config.json

# From an env file
kubectl create configmap app-config --from-env-file=.env
```

### Using ConfigMaps in Pods

#### Option 1: Individual Keys as Environment Variables

```yaml
spec:
  containers:
    - name: my-app
      image: my-image
      env:
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: database-host
        - name: DB_PORT
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: database-port
```

#### Option 2: All Keys as Environment Variables

```yaml
spec:
  containers:
    - name: my-app
      image: my-image
      envFrom:
        - configMapRef:
            name: app-config
        # prefix: APP_   # Optional: prefix all keys
```

> 💡 With `envFrom`, each key in the ConfigMap becomes an environment variable. `database-host` becomes `database-host` (with dashes, which may not work in all shells — use underscores in your ConfigMap keys!).

#### Option 3: Mount as Files

```yaml
spec:
  containers:
    - name: my-app
      image: my-image
      volumeMounts:
        - name: config-volume
          mountPath: /app/config       # Directory in the container
          readOnly: true
  volumes:
    - name: config-volume
      configMap:
        name: app-config
```

Each key becomes a file in `/app/config/`:
```
/app/config/
├── database-host        # content: "mongodb-service"
├── database-port        # content: "27017"
├── story-folder         # content: "story"
├── log-level            # content: "info"
└── app-config.json      # content: the JSON object
```

### ConfigMap vs Secret vs Environment Variable

| Feature | Hardcoded `env` | ConfigMap | Secret |
|---------|----------------|-----------|--------|
| **Defined in** | Pod spec | Separate resource | Separate resource |
| **Encoding** | Plain text | Plain text | Base64 encoded |
| **Reusable** | ❌ | ✅ Across Pods | ✅ Across Pods |
| **Updatable** | Requires Pod restart | Can update in-place* | Can update in-place* |
| **Best for** | Static, pod-specific values | Configuration, feature flags | Passwords, API keys, tokens |

> \* Mounted ConfigMaps update automatically (with a delay). Environment variables from ConfigMaps require a Pod restart.

### Applying Everything

```bash
# Apply the ConfigMap first
kubectl apply -f configmap.yaml

# Then the deployment that references it
kubectl apply -f deployment.yaml

# Verify ConfigMap
kubectl get configmap
kubectl describe configmap app-config
```

---

## Summary — Key Takeaways

1. **Kubernetes Volumes** are more powerful than Docker volumes — supporting many backends and flexibility
2. **emptyDir** = temporary, Pod-scoped storage that survives container restarts but not Pod deletion
3. **hostPath** = node-level storage useful for development but unsafe for multi-node production
4. **CSI** = standardized interface for plugging in any storage backend
5. **Persistent Volumes (PV)** = cluster-level storage defined by admins
6. **Persistent Volume Claims (PVC)** = developer requests for storage, bound to PVs
7. **StorageClasses** enable dynamic provisioning — no manual PV creation needed
8. **Environment Variables** can be hardcoded, from ConfigMaps, Secrets, or the downward API
9. **ConfigMaps** decouple configuration from container images — the K8s way of managing config

---

[← Kubernetes in Action](./kubernetes-in-action.md) | [Back to Index](./README.md) | [Next: Kubernetes Networking →](./kubernetes-networking.md)
