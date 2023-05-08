import streamlit as st
import os
import base64

def main():
    # st.title('Video Viewer')

    video_file_path = r"C:\Users\pc\Documents\GitHub\video_sharing\videoplayback.webm"

    if video_file_path and os.path.isfile(video_file_path) and video_file_path.lower().endswith((".mp4", ".mov", ".avi", ".mkv", ".webm")):
        with open(video_file_path, "rb") as file:
            video_data = base64.b64encode(file.read()).decode("utf-8")
        video_type = os.path.splitext(video_file_path)[-1].replace(".", "")
        st.markdown(f"""
            <video width="125%" height="auto" controls loop>
                <source src="data:video/{video_type};base64,{video_data}" type="video/{video_type}">
            </video>
        """, unsafe_allow_html=True)
    elif video_file_path:
        st.error("Invalid video file path. Please check the file path and the file extension.")

if __name__ == "__main__":
    main()
