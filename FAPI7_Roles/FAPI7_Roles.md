|||
|---|---|
|ДИСЦИПЛИНА|Технологии разработки серверных приложений|
|ИНСТИТУТ|ИПТИП|
|КАФЕДРА|Индустриального программирования|
|ВИД УЧЕБНОГО МАТЕРИАЛА|Методические указания к практическим занятиям|
|ПРЕПОДАВАТЕЛЬ|Дворецкий Артур Геннадьевич, Александров Алексей Сергеевич|
|СЕМЕСТР|4 семестр, 2025/2026 уч. год|

Ссылка на материал: <br>
https://github.com/dv0retsky/fastapi-tutorial/blob/main/FAPI7_Roles/FAPI7_Roles.md

---

# Практическое занятие №7: Управление доступом на основе ролей 🌲

**Управление доступом на основе ролей (RBAC - Role Based Access Control)** — это подход, который используется для управления правами доступа в приложениях. В основе **RBAC** лежит разделение пользователей на группы, или роли, с соответствующими правами.

<div align="center">
  <img alt="Project Demo" src="./mygif/gif7-1.gif" />
</div>

Как это работает? Представь, что твое веб-приложение — это большой офис, в котором есть разные сотрудники. У каждого сотрудника есть своя роль: кто-то работает в бухгалтерии, кто-то в отделе продаж, а кто-то в техническом отделе. У каждой роли есть доступ к определенным ресурсам. Например, бухгалтеру разрешено видеть и изменять финансовые данные, а сотруднику отдела продаж — только данные клиентов.

**Важное преимущество RBAC** — это централизованное управление правами доступа. Ты можешь назначить роль пользователю и предоставить доступ к нужным ресурсам, не заботясь о том, кто конкретно этот пользователь, а просто полагаясь на его роль в системе.

Использование **RBAC** помогает избежать несанкционированного доступа и упрощает управление правами доступа.

## 🌳 Компоненты RBAC

**RBAC** состоит из трех основных компонентов, которые помогают организовать и управлять доступом в приложении:

- **Роли** — это категории, которые определяют, какие действия доступны пользователю. Роль может быть связана с обязанностями в организации или с функциональностью приложения. Например, роль "администратор" может включать полный доступ ко всем функциям, а роль "пользователь" — только доступ к просмотру данных.

- **Разрешения** — это конкретные действия или операции, которые пользователь может выполнять в приложении. Разрешения могут быть такими, как "чтение", "запись", "удаление" и т.д. Например, разрешение "чтение" позволяет просматривать информацию, а разрешение "запись" — вносить изменения в данные.

- **Пользователи** — это люди, которым назначаются роли. Один пользователь может иметь одну или несколько ролей, в зависимости от того, какой доступ ему необходим для выполнения своих задач. Например, сотрудник, который работает как администратор и пользователь, может иметь обе роли, предоставляющие различные уровни доступа.

Эти компоненты вместе обеспечивают гибкую систему управления доступом, минимизируя риск несанкционированного доступа.

## 🌵 Внедрение RBAC в FastAPI

Для реализации **RBAC** в **FastAPI** используется сочетание аутентификации (например, **JWT**) и авторизации, основанной на ролях. Вот обзор шагов по внедрению **RBAC**:

- **Шаг 1: Определите роли и разрешения.** Прежде чем внедрять **RBAC**, нужно определить, какие роли будут доступны в вашем приложении. Например, можно использовать такие роли, как "администратор", "пользователь" и "гость". Каждая роль будет иметь набор разрешений, которые определяют, что пользователь с этой ролью может делать в системе.

- **Шаг 2: Свяжите роли с пользователями.** После определения ролей, необходимо назначить их пользователям. Это можно сделать во время регистрации, при добавлении новых пользователей, или в процессе авторизации, когда пользователи логинятся в систему. Например, администратор может иметь роль "администратор", а обычный пользователь — роль "пользователь".

- **Шаг 3: Авторизация на основе ролей.** После того как пользователю назначена роль, нужно реализовать логику авторизации. Она будет проверять роль пользователя и определять, может ли он получить доступ к защищенным маршрутам или выполнить определенные действия. Например, администратор может иметь доступ ко всем функциям, а обычный пользователь — только к части функционала (например, к чтению данных или обновлению их).

## 🐢 Обработка доступа на основе ролей

**FastAPI** предлагает несколько способов управления доступом на основе ролей:

- **Внедрение зависимостей.** **FastAPI** позволяет создавать пользовательские зависимости, которые могут проверять роль пользователя перед предоставлением доступа к определенным конечным точкам. Это позволяет гибко управлять доступом и применять логику проверки ролей в нужных местах приложения.

- **Авторизация на основе декоратора.** Вы можете использовать декораторы для определения авторизации на основе ролей для конкретных конечных точек. Это упрощает процесс управления доступом и позволяет легко настраивать роли, которым разрешен доступ к тем или иным ресурсам.

- **Интеграция с базой данных.** Для более масштабных приложений стоит интегрировать систему **RBAC** с базой данных, где будут храниться роли пользователей и связанные с ними разрешения. Это позволяет динамически управлять доступом в зависимости от изменений в базе данных.

## 🍋‍🟩 Реализация управления доступом на основе ролей (RBAC) в FastAPI для начинающих

На данном занятии мы создадим простую систему контроля доступа с ролями `"admin"` и `"user"` с использованием **FastAPI**. Администраторы будут иметь доступ ко всем маршрутам, включая те, что предназначены для обычных пользователей. Мы будем использовать **JWT** для аутентификации и декораторы для авторизации.

### 🌴 Структура проекта

```bash
.
├── main.py               # Основной файл с FastAPI-приложением
├── security.py           # Функции для работы с JWT и аутентификацией
├── models.py             # Pydantic-схемы для данных
├── db.py                 # "База данных" для хранения пользователей
├── rbac.py               # Логика работы с RBAC и декораторы для проверки ролей
└── dependencies.py       # Общие зависимости, включая получение текущего пользователя
```

### 🥝 `security.py` – работа с JWT

```python
import jwt
import datetime
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends

# Определяем схему аутентификации (OAuth2 с паролем)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Секретный ключ для подписи JWT  
# В реальном проекте храните его в .env файле, а не в коде!
SECRET_KEY = "mysecretkey"  # Генерируем через `openssl rand -hex 32`
ALGORITHM = "HS256"  # Используем HMAC SHA-256 для подписи
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # Время жизни токена (15 минут)

def create_jwt_token(data: dict):
    """Создаём JWT-токен с указанием времени истечения"""
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # Добавляем время истечения в токен
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_from_token(token: str = Depends(oauth2_scheme)):
    """Получаем информацию о пользователе из токена"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Декодируем токен
        return payload.get("sub")  # JWT-токен содержит `sub` (subject) — имя пользователя
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Токен устарел")  # Токен просрочен
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Ошибка авторизации")  # Невалидный токен
```

### 🪀 `models.py` – модели данных Pydantic

```python
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """Модель пользователя с базовыми полями"""
    username: str
    full_name: str | None = None
    email: EmailStr | None = None
    disabled: bool = False
    roles: list[str]  # Список ролей пользователя

class UserLogin(BaseModel):
    """Модель для входа в систему"""
    username: str
    password: str
```

### 🥑 `db.py` – имитация базы данных

```python
from models import User

# Фиктивные данные пользователей (в реальном проекте тут будет БД)
USERS_DATA = [
    {
        "username": "admin",
        "password": "adminpass",  # В продакшене пароли должны быть хешированы!
        "roles": ["admin"],
        "full_name": "Admin User",
        "email": "admin@example.com",
        "disabled": False
    },
    {
        "username": "user",
        "password": "userpass",
        "roles": ["user"],
        "full_name": "Regular User",
        "email": "user@example.com",
        "disabled": False
    },
]

def get_user(username: str) -> User:
    """Получаем пользователя по имени (без пароля)"""
    for user_data in USERS_DATA:
        if user_data["username"] == username:
            return User(**{k: v for k, v in user_data.items() if k != "password"})
    return None
```

### 🍀 `rbac.py` – проверка прав доступа

```python
from fastapi import HTTPException, status
from functools import wraps

class PermissionChecker:
    """Декоратор для проверки ролей пользователя"""
    def __init__(self, roles: list[str]):
        self.roles = roles  # Список разрешённых ролей

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user = kwargs.get("current_user")  # Получаем текущего пользователя
            if not user:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Требуется аутентификация")

            if "admin" in user.roles:  # Админ всегда имеет доступ ко всему
                return await func(*args, **kwargs)

            if not any(role in user.roles for role in self.roles):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Недостаточно прав для доступа"
                )
            return await func(*args, **kwargs)
        return wrapper
```

### 🥦 `dependencies.py` – вспомогательные функции

```python
from fastapi import Depends, HTTPException, status
from security import get_user_from_token
from db import get_user
from models import User

def get_current_user(current_username: str = Depends(get_user_from_token)) -> User:
    """Получаем текущего пользователя по имени из токена"""
    user = get_user(current_username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
```

### 🦎 `main.py` – основное приложение

```python
from fastapi import FastAPI, Depends, HTTPException, status
from security import create_jwt_token
from models import UserLogin, User
from db import USERS_DATA
from dependencies import get_current_user
from rbac import PermissionChecker

app = FastAPI()

@app.post("/login")
async def login(user_in: UserLogin):
    """Маршрут для аутентификации"""
    for user in USERS_DATA:
        if user["username"] == user_in.username and user["password"] == user_in.password:
            # Генерируем JWT-токен для пользователя
            token = create_jwt_token({"sub": user_in.username})
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверные учетные данные")

@app.get("/admin")
@PermissionChecker(["admin"])
async def admin_info(current_user: User = Depends(get_current_user)):
    """Маршрут для администраторов"""
    return {"message": f"Hello, {current_user.username}! Welcome to the admin page."}

@app.get("/user")
@PermissionChecker(["user"])
async def user_info(current_user: User = Depends(get_current_user)):
    """Маршрут для пользователей"""
    return {"message": f"Hello, {current_user.username}! Welcome to the user page."}

@app.get("/about_me")
async def about_me(current_user: User = Depends(get_current_user)):
    """Информация о текущем пользователе"""
    return current_user
```

### 🥒 Дополнительные рекомендации

- **Хранение паролей:** Всегда используйте хэширование (например, библиотеку `Passlib`).
- **Минимальная длина пароля:** Не менее `12` символов с комбинацией букв, цифр и специальных символов.
- **Реальная база данных:** Для продакшена замените USERS_DATA на подключение к БД (PostgreSQL, MySQL и т. д.).

### 🧃 Тестирование

Авторизация администратора:

```bash
curl -X POST http://localhost:8000/login -H "Content-Type: application/json" -d '{"username":"admin","password":"adminpass"}'
```

Доступ к защищённым эндпоинтам:

```bash
# Для администратора
curl -H "Authorization: Bearer {TOKEN}" http://localhost:8000/admin

# Для пользователя
curl -H "Authorization: Bearer {TOKEN}" http://localhost:8000/user
```

---

Теперь у вас есть базовое понимание, как реализовать **RBAC** в **FastAPI**, и вы можете адаптировать эту систему под свои нужды.

---

## 🌿 Расширенная система RBAC: миграция на разрешения (Permissions)

Базовая система **RBAC** на основе ролей хорошо работает для простых случаев, но имеет ограничения:

- Нельзя дать пользователю дополнительные права сверх его роли
- Проверяется вся роль целиком, а не конкретное действие
- Сложно управлять гранулярными правами доступа

Давайте расширим систему, чтобы она работала с **разрешениями** (permissions) вместо прямой проверки ролей. Это позволит:

1. Гибко назначать права — за каждой ролью будут закреплены свои разрешения, которые можно в любой момент отредактировать, без изменения по всему коду.  
    Например, староста группы и преподаватель имеют возможность ставить "+", "н" и "у" студентам своей группы, но потом вы решаете, что возможность ставить "у" должна быть только у учебного отдела.  
    В такой ситуации, если система завязана на ролях, необходимо менять код программы и перезапускать систему. Однако разрешения позволяют изменить это "на лету" - достаточно просто изменить список разрешений для роли "староста". Такой подход позволяет гибко управлять системой администратору.


2. Возможность выдачи персональных доступов конкретному пользователю навсегда, иди на время. Например, преподаватель может выдать старосте доступ на отметку студентов в электронном журнале на 15 минут. В таком случае доступ получают не все пользователи с ролью "староста", а один конкретный пользователь.

Для реализации такой системы нужно расширить текущий вариант.

### 🍃 Шаг 1: Создаем перечисление разрешений

Первым делом определяем **все возможные разрешения** в системе. Используем `Enum` для строгой типизации:

**`models.py` — добавляем Permissions:**

```python
from pydantic import BaseModel, EmailStr, Field, model_validator
from enum import Enum


class Permissions(str, Enum):
    """перечисление всех разрешений в системе"""
    READ_USERS = "read:users"
    WRITE_USERS = "write:users"
    DELETE_USERS = "delete:users"
    READ_ADMIN = "read:admin"
    WRITE_ADMIN = "write:admin"
    READ_REPORTS = "read:reports"
    WRITE_REPORTS = "write:reports"
```

Мы используем формат `"действие:ресурс"` для ясности и читаемости кода — это позволяет сразу понять, какое именно действие разрешено выполнять над каким ресурсом. 

Наследование от `str, Enum` позволяет использовать значения перечисления как обычные строки, что упрощает работу с ними в коде и базе данных. 

Централизованное хранение всех разрешений в одном месте делает систему легко управляемой: при необходимости добавить новое разрешение или изменить существующее, достаточно внести изменения в одно место, и они автоматически применятся во всей системе.

### 🌾 Шаг 2: Связываем роли с разрешениями

Теперь **роль** — это не просто строка, а объект с набором разрешений:

**`models.py` — добавляем класс Role:**

```python
class Role(BaseModel):
    """роль содержит название и список разрешений"""
    name: str
    permissions: list[str]
```

**`db.py` — создаём реестр ролей:**

```python
from models import User, Role, Permissions

# реестр ролей с их разрешениями
ROLES_REGISTRY = {
    "admin": Role(
        name="admin",
        permissions=[
            Permissions.READ_ADMIN,
            Permissions.WRITE_ADMIN,
            Permissions.READ_USERS,
            Permissions.WRITE_USERS,
            Permissions.DELETE_USERS,
            Permissions.READ_REPORTS,
            Permissions.WRITE_REPORTS,
        ]
    ),
    "user": Role(
        name="user",
        permissions=[
            Permissions.READ_USERS,
            Permissions.READ_REPORTS,
        ]
    ),
    "moderator": Role(
        name="moderator",
        permissions=[
            Permissions.READ_USERS,
            Permissions.WRITE_USERS,
            Permissions.READ_REPORTS,
            Permissions.WRITE_REPORTS,
        ]
    ),
}
```

**Что изменилось?**  
- **admin** — все разрешения (полный доступ, как и было раньше)
- **user** — только чтение (минимальный доступ)
- **moderator** — чтение + запись (без возможности удаления и администрирования)

### 🌱 Шаг 3: Модифицируем User для работы с разрешениями

Пользователь теперь автоматически получает все разрешения из своих ролей + может иметь дополнительные за счёт использования `set` для хранения разрешений и возможности добавления персональных прав через `extra_permissions`.

Когда пользователь создаётся, система автоматически собирает все разрешения из его ролей в единую коллекцию типа `set`.

В отличие от ролей, для разрешений используется `set` вместо `list`, потому что `set` гарантирует уникальность элементов и убирает дубликаты, в случае, если у разных ролей будут одинаковые разрешения.

Помимо разрешений, добавляемых пользователю из ролей, система поддерживает `extra_permissions` — персональные права, которые можно назначить конкретному пользователю независимо от его ролей. 

Это решает проблему, когда нужно дать одному человеку дополнительное разрешение, не меняя при этом всю роль и не создавая новую роль ради одного исключения. Например, обычный пользователь с ролью `user` может получить право `write:reports` через `extra_permissions`, не становясь при этом модератором.

**`models.py` — обновляем класс User:**

```python
class User(BaseModel):
    username: str
    full_name: str | None = None
    email: EmailStr | None = None
    disabled: bool = False
    roles: list[str]  # список ролей остаётся
    permissions: set[str] = Field(default_factory=set)  # разрешения автоматически
    extra_permissions: list[str] = Field(default_factory=list)  # дополнительные разрешения
    
    @model_validator(mode='after')
    def populate_permissions(self):
        """автоматически собираем все разрешения при создании пользователя"""
        from db import ROLES_REGISTRY
        
        # собираем все разрешения из ролей
        all_permissions = set()
        for role_name in self.roles:
            if role_name in ROLES_REGISTRY:
                role = ROLES_REGISTRY[role_name]
                all_permissions.update(role.permissions)
        
        # добавляем дополнительные разрешения
        all_permissions.update(self.extra_permissions)
        
        self.permissions = all_permissions
        return self
```

**Как это работает?**  
1. При создании объекта User вызывается `populate_permissions`
2. Проходимся по всем ролям пользователя
3. Собираем разрешения из каждой роли в `set` (для уникальности)
4. Добавляем `extra_permissions` — персональные разрешения
5. Результат сохраняется в `user.permissions`

**Пример пользователя с дополнительными разрешениями:**

```python
# в USERS_DATA добавляем:
{
    "username": "special_user",
    "password": "specialpass",
    "roles": ["user"],  # базовая роль
    "full_name": "Special User",
    "email": "special@example.com",
    "disabled": False,
    "extra_permissions": [Permissions.WRITE_REPORTS]  # дополнительное разрешение!
}
```

Этот пользователь получит:
- `read:users` и `read:reports` — из роли "user"
- `write:reports` — дополнительное разрешение

### 🍂 Шаг 4: Модифицируем PermissionChecker

Теперь декоратор проверяет **разрешения**, а не роли:

**`rbac.py` — обновляем PermissionChecker:**

```python
from fastapi import HTTPException, status
from functools import wraps

class PermissionChecker:
    """декоратор для проверки разрешений пользователя"""
    def __init__(self, required_permissions: list[str]):
        self.required_permissions = required_permissions  # теперь это разрешения, а не роли

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user = kwargs.get("current_user")
            if not user:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Требуется аутентификация")

            # проверяем наличие хотя бы одного требуемого разрешения
            if not any(perm in user.permissions for perm in self.required_permissions):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Недостаточно прав для доступа. Требуется одно из разрешений: {', '.join(self.required_permissions)}"
                )
            return await func(*args, **kwargs)
        return wrapper
```

Для этого мы:
- Меняем параметры: `roles` → `required_permissions`
- Заменяем проверку: `perm in user.permissions` вместо `role in user.roles`

Теперь нам не нужно проверять, является ли пользователь админом, или нет - у админа и так есть все права.

### 🌸 Шаг 5: Обновляем эндпоинты

Теперь указываем **конкретные разрешения** для каждого эндпоинта:

**`main.py` — примеры использования:**

```python
from fastapi import FastAPI, Depends, HTTPException, status
from security import create_jwt_token
from models import UserLogin, User, Permissions
from db import USERS_DATA
from dependencies import get_current_user
from rbac import PermissionChecker

app = FastAPI()

@app.post("/login")
async def login(user_in: UserLogin):
    for user in USERS_DATA:
        if user["username"] == user_in.username and user["password"] == user_in.password:
            token = create_jwt_token({"sub": user_in.username})
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверные учетные данные")

@app.get("/admin")
@PermissionChecker([Permissions.READ_ADMIN])  # требуется разрешение read:admin
async def admin_info(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! Welcome to the admin page."}

@app.get("/users")
@PermissionChecker([Permissions.READ_USERS])  # требуется разрешение read:users
async def read_users(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! Here is the list of users."}

@app.post("/users")
@PermissionChecker([Permissions.WRITE_USERS])  # требуется разрешение write:users
async def write_users(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You can create/update users."}

@app.delete("/users/{user_id}")
@PermissionChecker([Permissions.DELETE_USERS])  # требуется разрешение delete:users
async def delete_users(user_id: int, current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You deleted user {user_id}."}

@app.get("/about_me")
async def about_me(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "roles": current_user.roles,
        "permissions": list(current_user.permissions)  # показываем все разрешения
    }
```

### 🧪 Тестирование системы с разрешениями

Авторизация пользователя `special_user` (роль "user" + дополнительное разрешение `write:reports`):

```bash
curl -X POST http://localhost:8000/login -H "Content-Type: application/json" -d '{"username":"special_user","password":"specialpass"}'
```

Результат:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Проверка разрешений пользователя:

```bash
curl -H "Authorization: Bearer {TOKEN}" http://localhost:8000/about_me
```

Результат покажет список всех разрешений пользователя:
```json
{
  "username": "special_user",
  "roles": ["user"],
  "permissions": ["read:users", "read:reports", "write:reports"]
}
```

Попытка записи отчёта — **успешно** (есть дополнительное разрешение `write:reports`):

```bash
curl -X POST -H "Authorization: Bearer {TOKEN}" http://localhost:8000/reports
```

Результат:
```json
{
  "message": "Hello, special_user! You can create/update reports."
}
```

Попытка записи пользователей — **ошибка** (нет разрешения `write:users`):

```bash
curl -X POST -H "Authorization: Bearer {TOKEN}" http://localhost:8000/users
```

Результат:
```json
{
  "detail": "Недостаточно прав для доступа. Требуется одно из разрешений: write:users"
}
```

<div align="center">
  <img alt="Project Demo" src="./mygif/gif7-2.gif" />
</div>

Теперь у вас есть **продвинутая система RBAC** на основе разрешений, которая легко масштабируется и обеспечивает гибкий контроль доступа! 🎉

---

<div align="center"> Made with ❤️ by <b>dv0retsky & AlexeyAleksandrov</b> </div>