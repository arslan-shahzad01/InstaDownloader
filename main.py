import streamlit as st
import yt_dlp
import os

def download_reel(url):
    output_path = "downloads"
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'best',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    
    return filename

st.title("Instagram Reel Downloader")

url = st.text_input("Enter Reel URL:")

if st.button("Download"):
    if url:
        try:
            file_path = download_reel(url)
            with open(file_path, "rb") as file:
                st.download_button(label="Click to Download", data=file, file_name=os.path.basename(file_path))
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")
