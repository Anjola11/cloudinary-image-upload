from fastapi import APIRouter, UploadFile
from cloudinary_service.services import UploadServices

cloudinary_router = APIRouter()
upload_services = UploadServices()


@cloudinary_router.post("/upload-image")
async def upload_image(file:UploadFile):
    file_url = await upload_services.upload_image(file)

    return {"url": file_url}