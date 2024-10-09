# Video Uploader with Transcript and Summary Generator

This application allows users to upload a video through a Streamlit interface. Once uploaded, the backend processes the video by extracting audio, generating a transcript using OpenAI's Whisper API, and then creating a summary using OpenAI's GPT-4 model. The application is built using Streamlit for the frontend and FastAPI for the backend.

# Demo Video Link
https://drive.google.com/file/d/16g-JRlaBOuDskOykYM7IF4UprrGmPJom/view?usp=sharing 

## Features
- Upload a video file through the Streamlit interface.
- Generate a transcript of the audio from the video using OpenAI Whisper.
- Generate a summary of the transcript using OpenAI's GPT-4 model.
- The backend provides JSON responses with both the transcript and summary.

## Getting Started

## Deployment

To deploy this project run:

First install the requirements

```bash
  pip install -r requirements.txt
```

Add your OpenAI API key to the .env file
```bash
  OPENAI_API_KEY=your_openai_api_key
```

## Running the Application
To start the fastapi backend:
```bash
  fastapi run app.py
```
To start the Streamlit:
```bash
  streamlit run streamlit.py 
```


