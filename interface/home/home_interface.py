from fastapi import APIRouter

home_router = APIRouter()


@home_router.get("/")
async def health_check():
    return {"msg": "backend pagamentos"}
