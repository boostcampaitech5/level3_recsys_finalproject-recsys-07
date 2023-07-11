from fastapi import APIRouter

router = APIRouter(prefix="/data")


@router.get("/")
def printData():
    return "Hello Data!"
