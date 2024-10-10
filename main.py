
from openai import OpenAI
import os
from dotenv import load_dotenv
from moviepy.editor import *

def video_to_speech(filename):
    # Load the mp4 file
    video = VideoFileClip(f"uploaded_videos/{filename}")
    AUDIO_DIRECTORY = "Converted_audio"


    if not os.path.exists(AUDIO_DIRECTORY):
        os.makedirs(AUDIO_DIRECTORY)
    # Extract audio from video
    video.audio.write_audiofile(f"Converted_audio/{filename[:-4]}.mp3")

def processor(filename):
    
    print("Extracting audio from video")
    video_to_speech(filename)
    print("Extraction completed")
    
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # API key stored in .env
   
    print("Starting Speech to text using Whisper model")
    client = OpenAI()

    # Used the OpenAI Whisper model API for speech to text covertion
    # Did not run the model locally using hugging face due to hardware contrainsts and long inference time
    audio_file= open(f"Converted_audio/{filename[:-4]}.mp3", "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    print("Completed transcription")
    
    # Used gpt-4o mini model for summary generation
    MODEL="gpt-4o-mini"
    completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Just create a summary for whatever text is given to you, create a technical summary"}, # <-- This is the system message that provides context to the model
        {"role": "user", "content": transcription.text} 
    ]
    )
    print("Summary generated")

    response=str(completion.choices[0].message.content)
    return (str(transcription.text), str(response))
