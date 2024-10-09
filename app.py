from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from main import processor
import os

app = FastAPI()

UPLOAD_DIRECTORY = "uploaded_videos"


if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.post("/upload-video/")
async def upload_video(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)

    # Save the uploaded video to the specified location
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())


    transcription, summary= processor(file.filename) #getting the transcript and summary from the processory function
    
    
    processing_result = {
        "transcription": transcription,
        "summary": summary,
       
    }

    return JSONResponse(content=processing_result)  # Returning Json response




