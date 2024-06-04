from fastapi import APIRouter
from fastapi.responses import JSONResponse
from service.admin_service import AdminService

from service.user_service import UserService
from utils.utils import verify_password, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dto.token import Token
from dto.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AdminService()

# @router.get("/create-survery", response=SurveryResponse)
# def create_survary(data: Survery, user:User):
#     if "admin.survery" in user.permission:
#         try:
#             ...
#             #Llamada al servicio
#             return service.create_survery(data=data)
#         except Exception as e:
#             JSONResponse(status=500, content={"status":500, "data": f"Something goes wrong: {str(e)}"})

#     else:
#         JSONResponse(status=403, content={"status":403, "data": "Missing permission to perfor that action"})

 
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserService.get_user(username=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/create-user")
async def create_user(user: User):
    try:
        service = UserService()

        service.create_user(username=user.username, password=user.password, name=user.name)

        return {"message": "User created successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Something goes wrong: {str(e)}"})
