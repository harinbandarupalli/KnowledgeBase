# Section 8: A More Complex Setup — Laravel & PHP Dockerized Project

## 1. The Target Setup

A multi-container application with:

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│  Nginx  │───►│   PHP   │───►│  MySQL  │
│ (server)│    │ (app)   │    │  (DB)   │
└─────────┘    └─────────┘    └─────────┘
     ▲              ▲
     │              │
  Port 80     Bind Mount
              (source code)
```

Plus **utility containers** for Composer, Artisan, and npm.

---

## 2. Adding an Nginx (Web Server) Container

```yaml
# docker-compose.yml
services:
  server:
    image: nginx:stable-alpine
    ports:
      - "8000:80"
    volumes:
      - ./src:/var/www/html
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - php
      - mysql
```

---

## 3. Adding a PHP Container

```dockerfile
# dockerfiles/php.dockerfile
FROM php:8.1-fpm-alpine
WORKDIR /var/www/html
RUN docker-php-ext-install pdo pdo_mysql
```

```yaml
# In docker-compose.yml
  php:
    build:
      context: .
      dockerfile: dockerfiles/php.dockerfile
    volumes:
      - ./src:/var/www/html:delegated
```

---

## 4. Adding a MySQL Container

```yaml
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: laravel
      MYSQL_USER: laravel
      MYSQL_PASSWORD: secret
      MYSQL_ROOT_PASSWORD: secret
    volumes:
      - db-data:/var/lib/mysql
```

---

## 5. Adding Utility Containers

```yaml
  # Composer (PHP dependency manager)
  composer:
    build:
      context: ./dockerfiles
      dockerfile: composer.dockerfile
    volumes:
      - ./src:/var/www/html
    entrypoint: ["composer"]

  # Artisan (Laravel CLI)
  artisan:
    build:
      context: .
      dockerfile: dockerfiles/php.dockerfile
    volumes:
      - ./src:/var/www/html
    entrypoint: ["php", "/var/www/html/artisan"]

  # npm (for frontend assets)
  npm:
    image: node:18-alpine
    working_dir: /var/www/html
    volumes:
      - ./src:/var/www/html
    entrypoint: ["npm"]

volumes:
  db-data:
```

---

## 6. Creating a Laravel App via Composer

```bash
docker compose run --rm composer create-project laravel/laravel .
```

---

## 7. Running the Full Stack

```bash
# Start only the app services
docker compose up -d server php mysql

# Run migrations
docker compose run --rm artisan migrate

# Install frontend deps
docker compose run --rm npm install
```

---

## 8. Launching Only Some Services

```bash
# Only start specific services
docker compose up -d server php mysql

# Utility containers are run on-demand
docker compose run --rm artisan migrate
docker compose run --rm npm run dev
```

---

## 9. Bind Mounts vs COPY — When To Use What

| Scenario | Use |
|----------|-----|
| **Development** | Bind mounts — live code sync |
| **Production** | `COPY` — bake code into image |
| **Utility containers** | Bind mounts — tools write to host |
| **Dependencies** | `COPY` at build + anonymous volume to protect |

---

## 10. Docker Compose With and Without Dockerfiles

| Approach | When to Use |
|----------|-------------|
| `image:` only | Pre-built images (nginx, mysql, mongo) |
| `build:` + Dockerfile | Custom images (your app, PHP with extensions) |
| Mix of both | Most real projects |
