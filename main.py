import yt_dlp
import streamlit as st


def main():
    st.title("Video Downloader")

    # Header
    st.header("Welcome to Video Downloader App")
    st.subheader("Download your favorite YouTube videos!")

    # Input field for the video URL
    url_to_download = st.text_input("Enter the video URL to download Video : ")

    # Download the video if URL is provided
    if st.button("Download Video") and url_to_download:
        # Set options for yt_dlp
        ydl_opts = {}

        # Download the video

        progress_bar = st.progress(0)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url_to_download, download=False)
                video_title = info_dict.get('title', 'Video')
                st.write(f"Downloading: {video_title}")
                ydl.add_progress_hook(lambda d: progress_bar.progress(d['downloaded_bytes'] / d['total_bytes']) if d['status'] == 'downloading' else None)
                ydl.download([url_to_download])
                progress_bar.empty()
                st.success("Your Video Successfully Downloaded")

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Made with ❤️ by codewithdark")


if __name__ == "__main__":
    main()
