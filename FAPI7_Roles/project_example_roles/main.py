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
@PermissionChecker([Permissions.READ_ADMIN])
async def admin_info(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! Welcome to the admin page."}

@app.get("/admin/write")
@PermissionChecker([Permissions.WRITE_ADMIN])
async def admin_write(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You can write admin data."}

@app.get("/users")
@PermissionChecker([Permissions.READ_USERS])
async def read_users(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! Here is the list of users."}

@app.post("/users")
@PermissionChecker([Permissions.WRITE_USERS])
async def write_users(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You can create/update users."}

@app.delete("/users/{user_id}")
@PermissionChecker([Permissions.DELETE_USERS])
async def delete_users(user_id: int, current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You deleted user {user_id}."}

@app.get("/reports")
@PermissionChecker([Permissions.READ_REPORTS])
async def read_reports(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! Here are the reports."}

@app.post("/reports")
@PermissionChecker([Permissions.WRITE_REPORTS])
async def write_reports(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You can create/update reports."}

@app.get("/about_me")
async def about_me(current_user: User = Depends(get_current_user)):
    return {
        "username": current_user.username,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "roles": current_user.roles,
        "permissions": list(current_user.permissions)
    }
