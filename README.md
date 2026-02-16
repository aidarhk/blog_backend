# 🚀 FastAPI Blog API

[![Tests](https://img.shields.io/badge/tests-3/3%20passed-brightgreen)](http://localhost:8000/docs)
[![Docker](https://img.shields.io/badge/Docker-ready-blue)](http://localhost:8000/docs)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-yellow)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

с JWT-аутентификацией, админ-панелью, Docker контейнеризацией и автотестами.

## ✨ **Основные возможности**

- 🔐 **JWT аутентификация** (регистрация/логин)
- 🛠️ **Админ-панель** (CRUD посты/категории)
- 🌐 **Публичные роуты** (чтение постов/категорий)
- 🗄️ **SQLAlchemy + SQLite** (производственная БД)
- 🐳 **Docker** (одна команда для запуска)
- 🧪 **Pytest** автотесты (3/3 passed)
- 📚 **Swagger UI / ReDoc** (автодокументация)
- ✅ **Pydantic** валидация + HTML санитизация

## 🚀 **Быстрый старт (30 секунд)**

```bash
# 1. Клонировать проект
git clone https://github.com/aidarhk/blog_backend.git blog_backend
cd blog_backend

# 2. Запуск
docker-compose up --build -d

# 3. Открыть Swagger UI
http://localhost:8000/docs
```

🧪 Автотесты
```bash
docker-compose exec blog-api pytest tests/ -v
```

## Роль админа
После запуска docker можете выдать себе админа
```bash
docker-compose exec blog-api python make_admin.py
```
