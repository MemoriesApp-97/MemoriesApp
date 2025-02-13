import streamlit as st
import os
import base64

# 💖 Function to Set Background Image
def set_background(image_path):
    if os.path.exists(image_path):  # Check if file exists
        with open(image_path, "rb") as image:
            encoded_string = base64.b64encode(image.read()).decode()
        bg_image = f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
            }}
        </style>
        """
        st.markdown(bg_image, unsafe_allow_html=True)
    else:
        st.error("⚠️ Background image not found! Please check the file path.")

# ✅ Debugging: Check if Background Exists
if os.path.exists("background.jpg"):
    st.success("✅ Background image found!")
else:
    st.error("❌ Background image NOT found! Check the file path.")

# 🎨 Set Background Image (Use Full Path)
set_background(r"C:\Users\pratitee\OneDrive\Desktop\MemoriesApp\background.jpg")  

# ❤️ Valentine's Day Header
st.markdown("<h1 style='color:#D63384; text-align:center;'>💕 Our Love Story 💕</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color:#6A0572; text-align:center;'>A journey of beautiful memories together! 💑</h2>", unsafe_allow_html=True)

# 🌹 Dropdown for Year Selection
years = sorted(os.listdir("Memories")) if os.path.exists("Memories") else []
selected_year = st.selectbox("📅 Select a Year", years)

# Display Memories (Images & Videos)
if selected_year:
    image_extensions = [".png", ".jpg", ".jpeg"]
    video_extensions = [".mp4", ".mov", ".avi"]

    folder_path = os.path.join("Memories", selected_year)
    files = os.listdir(folder_path) if os.path.exists(folder_path) else []

    images = [f for f in files if any(f.lower().endswith(ext) for ext in image_extensions)]
    videos = [f for f in files if any(f.lower().endswith(ext) for ext in video_extensions)]

    st.markdown(f"<h2 style='color:#6A0572; text-align:center;'>💞 Memories from {selected_year} 💞</h2>", unsafe_allow_html=True)

    # Display Images
    for img in images:
        st.image(os.path.join(folder_path, img), caption=f"{selected_year} - {img}", use_column_width=True)

    # Display Videos
    for vid in videos:
        st.video(os.path.join(folder_path, vid))

# ✍️ Love Note
st.markdown(
    "<h3 style='color:#6A0572; text-align:center;'>🌟 Thank you for every moment we’ve shared! I love you! ❤️</h3>",
    unsafe_allow_html=True
)
