import yt_dlp
import streamlit as st
import os
from urllib3.exceptions import ReadTimeoutError

def main():
    # Header
    st.header("Welcome to Video Downloader App")
    st.subheader("Download your favorite YouTube videos!")

    # Input field for the video URL
    url_to_download = st.text_input("Enter the video URL to download Video : ")

    # Download the video if URL is provided
    if st.button("Download Video") and url_to_download:
        # Set options for yt_dlp
        ydl_opts = {}

        try:
            # Get the default downloads directory
            default_download_path = os.path.expanduser("~/Downloads")

            # Set the output path for downloaded video
            ydl_opts['outtmpl'] = os.path.join(default_download_path, '%(title)s.%(ext)s')


            # Start the download spinner
            with st.spinner("Downloading..."):
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url_to_download, download=True)

            st.success("Your Video Successfully Downloaded")

        except ReadTimeoutError:
            st.error("Please Check Your Connection. Please try again.")
        except Exception as e:
            st.error("Please Check Your Connection. Please try again.")

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Made with ❤️ by codewithdark")


if __name__ == "__main__":
    main()
