from fastapi import APIRouter, Depends, HTTPException, Request

router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@router.post("/process")
async def read_items(request: Request):
    print(request)
    return {"message": "Hello World"}
