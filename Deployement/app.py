import streamlit as st
import cv2
from ultralytics import YOLO

from auth.login import login_screen
from components import home, image_detection, video_detection, webcam_detection
from model.yolo_model import load_model_yolo

# Login check
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_screen()
    st.stop()

# Load YOLO model

model_yolo = load_model_yolo()

# Sidebar
st.set_page_config(page_title="🌾 FarmWise", layout="wide")
st.sidebar.image("https://cdn-icons-png.freepik.com/512/1886/1886966.png", width=100)
st.sidebar.title("🌾 FarmWise")
st.sidebar.markdown("Smart Detection for Farmers")

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.experimental_rerun()

# Page routing
page = st.sidebar.radio("📌 Navigate to:", ["🏡 Home", "📷 Image Detection", "🎥 Video Detection", "📹 Real-Time Webcam"])

if page == "🏡 Home":
    home.show()
elif page == "📷 Image Detection":
    image_detection.show(model_yolo)
elif page == "🎥 Video Detection":
    video_detection.show(model_yolo)
elif page == "📹 Real-Time Webcam":
    webcam_detection.show(model_yolo)
