from fastapi import FastAPI
from cloudinary_service.routes import cloudinary_router

app = FastAPI(
    title="Dvota API",
    description="Endpoints for Dvota",
)


app.include_router(cloudinary_router, prefix="/api/upload")

