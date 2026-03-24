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

USERS_DATA = [
    {
        "username": "admin",
        "password": "adminpass",
        "roles": ["admin"],
        "full_name": "Admin User",
        "email": "admin@example.com",
        "disabled": False,
        "extra_permissions": []
    },
    {
        "username": "user",
        "password": "userpass",
        "roles": ["user"],
        "full_name": "Regular User",
        "email": "user@example.com",
        "disabled": False,
        "extra_permissions": []
    },
    {
        "username": "moderator",
        "password": "modpass",
        "roles": ["moderator"],
        "full_name": "Moderator User",
        "email": "moderator@example.com",
        "disabled": False,
        "extra_permissions": []
    },
    {
        "username": "special_user",
        "password": "specialpass",
        "roles": ["user"],
        "full_name": "Special User",
        "email": "special@example.com",
        "disabled": False,
        "extra_permissions": [Permissions.WRITE_REPORTS]
    },
]

def get_user(username: str) -> User:
    for user_data in USERS_DATA:
        if user_data["username"] == username:
            return User(**{k: v for k, v in user_data.items() if k != "password"})
    return None
