# Odoo 17 Twitter QR Generator

## 📌 Project Overview

This project is a custom Odoo 17 application that generates QR codes for Twitter (X) profiles.

The application:
- Displays active Twitter accounts
- Automatically generates QR codes
- Allows users to download QR codes
- Is fully containerized using Docker
- Is deployed using Kubernetes with Kustomize overlays

---

## 🛠 Technologies Used

- Odoo 17
- Python (qrcode, Pillow)
- Docker
- Docker Compose
- Kubernetes
- Kustomize
- PostgreSQL 16

---

## 📂 Project Structure

```
addons/                     # Custom Odoo module
Dockerfile                  # Custom Odoo image
requirements.txt            # Python dependencies
docker-compose.yml          # Local development
k8s/
  ├── base/
  └── overlays/
README.md
```

---

# 🐳 Local Development (Docker Compose)

## 1️⃣ Build Custom Image

```bash
docker build -t chaoschrono/odoo-custom:1.0 .
```

## 2️⃣ Start Services

```bash
docker-compose up -d
```

## 3️⃣ Access Odoo

Open:

```
http://localhost:8067
```

---

# ☸ Kubernetes Deployment

## 1️⃣ Apply Local Overlay

```bash
kubectl apply -k k8s/overlays/local
```

## 2️⃣ Verify Pods

```bash
kubectl get pods
```

Expected:
- 1 Odoo pod (Running)
- 1 PostgreSQL pod (Running)

## 3️⃣ Port Forward

```bash
kubectl port-forward service/odoo-service 8069:80
```

## 4️⃣ Access Application

```
http://localhost:8069/twitter-qr
```

---

# 🔄 Updating the Module

If changes are made to templates or logic:

1. Go to **Apps**
2. Click **Update Apps List**
3. Upgrade the `twitter_qrcode` module

No database recreation required.

---

# 🗄 Kubernetes Resources Included

- Deployment (Odoo)
- StatefulSet (PostgreSQL)
- Service (ClusterIP)
- ConfigMap
- Secret
- PersistentVolumeClaim
- Kustomize overlays for:
  - local
  - dev
  - test
  - prod

---

# 👤 Author

Curt Coetzee