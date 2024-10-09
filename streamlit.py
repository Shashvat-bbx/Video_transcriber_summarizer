import streamlit as st
import requests


backend_url = "http://127.0.0.1:8000/upload-video/"

st.title("Video Upload and Processing with FastAPI Backend")

# Upload the video
uploaded_video = st.file_uploader("Upload an MP4 video", type=["mp4"])

if uploaded_video is not None:
    st.video(uploaded_video)
    
    # Convert the uploaded video file to bytes
    files = {'file': (uploaded_video.name, uploaded_video.read(), 'video/mp4')}
    
    # Send the video to FastAPI backend and process it
    with st.spinner("Uploading and processing..."):
        response = requests.post(backend_url, files=files)
        
        if response.status_code == 200:
            st.success("Video uploaded and processed successfully!")
            processing_result = response.json()  # Get JSON response from backend
            
            # Display the processing result
            st.write("**Processing Results**")
            st.write(f"**The Transcript of the video is as follows:**")
            st.write(f"\n{processing_result['transcription']}")
            st.write(f"**The summary of the video is as follows:**")
            st.write(f" {processing_result['summary']}")
        else:
            st.error("Failed to upload or process the video.")
