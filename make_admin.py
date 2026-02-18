#!/usr/bin/env python3
"""
make_admin.py - Создать/обновить админа в БД
Запуск: python make_admin.py
"""

import sqlite3
import getpass
from app.core.security import get_password_hash

def make_admin():
    print("🔧 Создание/обновление админа")
    print("-" * 40)
    
    email = input("📧 Email (admin@test.com): ").strip() or "admin@test.com"
    password = getpass.getpass("🔑 Пароль: ").strip()
    
    if not email or not password:
        print("❌ Email и пароль обязательны!")
        return
    
    try:
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()
        
        hashed_password = get_password_hash(password)
        
        # UPSERT (создать или обновить)
        cursor.execute("""
            INSERT OR REPLACE INTO users (email, hashed_password, role) 
            VALUES (?, ?, 'ADMIN')
        """, (email, hashed_password))
        
        conn.commit()
        conn.close()
        
        print(f"\n✅ Админ '{email}' успешно создан/обновлён!")
        print(f"📱 Логин: {email}")
        print(f"🔑 Пароль: {password}")
        print("\n🚀 Перезапустите Docker: docker-compose restart")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    make_admin()
