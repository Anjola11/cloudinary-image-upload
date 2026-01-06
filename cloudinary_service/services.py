from config  import Config
from fastapi import UploadFile, HTTPException, status
import cloudinary
from cloudinary.uploader import upload
import asyncio

cloudinary.config(
    cloud_name=Config.CLOUDINARY_CLOUD_NAME,
    api_key=Config.CLOUDINARY_API_KEY,
    api_secret=Config.CLOUDINARY_API_SECRET
)

class UploadServices():

    def validate_file(self, file:UploadFile):

        allowed_types = ["image/jpeg", "image/jpg","image/png","image/webp"]

        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid file type, only jpeg, png, jpg, webp"
            )

        #set max size to 2mb
        max_bytes = 2 * 1024 * 1024

        #change the "cursor" position to the end of the file
        file.file.seek(0, 2)

        #get the file size
        file_size = file.file.tell()

        #change the "cursor" position to the beginning of the file, so that cloudinary can read the full file
        file.file.seek(0)

        if file_size > max_bytes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="file should not be greater than 2mb"
            )
        
    async def upload_image(self, file: UploadFile):
        
        self.validate_file(file)
        try:

            #run it on a separate thread to prevent blocking
            response = await asyncio.to_thread(upload,
                file=file.file,
                folder="test"
            )

            file_url = response['secure_url']
            return file_url

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=f"Error uploading images: {e}"
                )
