import streamlit as st
import time

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Chetan Sharma | Portfolio", layout="wide", page_icon="🎬")

# Custom CSS for Sleek Dark UI
st.markdown("""
    <style>
    .stApp { background-color: #0b0d10; }
    .construction-text { color: #ffcc00; font-size: 24px; font-weight: bold; text-align: center; }
    .main-title { color: #00e6ff; font-size: 35px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MODULES (FUNCTIONS) ---

def show_under_construction(section_name):
    """Har section ke liye professional animation aur message"""
    st.markdown(f"<div class='main-title'>{section_name}</div>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Lottie animation ki jagah hum Streamlit ka native spinner aur warning use karenge
        st.warning(f"🚧 This **{section_name}** section is currently under construction.")
        with st.status("Fetching latest edits...", expanded=True):
            st.write("Optimizing high-retention assets...")
            time.sleep(1)
            st.write("Polishing visual elements...")
            time.sleep(1)
        st.info("Bhai, thoda sabar rakho! Ek dum 'Elite' kaam render ho raha hai. 🔥")
        st.image("https://via.placeholder.com/600x300.png?text=Coming+Soon+...+Working+on+Quality", use_container_width=True)

def show_overview():
    st.markdown("<div class='main-title'>Chetan Sharma</div>", unsafe_allow_html=True)
    st.write("### Digital Creator & Tech Architect")
    st.write("Hathras se Global tak ka safar. Building high-impact digital assets.")
    st.write("---")
    st.success("✅ Dashboard Live & Responsive")

def show_connect():
    st.markdown("<div class='main-title'>Connect with Me</div>", unsafe_allow_html=True)
    st.write("Let's build something legendary together.")
    st.link_button("LinkedIn Profile", "https://linkedin.com")
    st.info("Email: workwithchetansharma@gmail.com")

# --- 3. MAIN APP LOGIC (ROUTING) ---

def main():
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("<h2 style='color: #00e6ff;'>📂 Menu</h2>", unsafe_allow_html=True)
        choice = st.radio("Select Section:", [
            "🏠 Home Overview", 
            "🎬 Video Editing", 
            "📸 Photo Editing", 
            "📊 Social Media Mgmt", 
            "✍️ Content Writing",
            "🌐 Connect"
        ])
        st.markdown("---")
        st.write("v1.2 | Powered by Python")

    # Routing Logic
    if choice == "🏠 Home Overview":
        show_overview()
    elif choice == "🎬 Video Editing":
        show_under_construction("Video Editing")
    elif choice == "📸 Photo Editing":
        show_under_construction("Photo Editing")
    elif choice == "📊 Social Media Mgmt":
        show_under_construction("Social Media Management")
    elif choice == "✍️ Content Writing":
        show_under_construction("Content Writing")
    elif choice == "🌐 Connect":
        show_connect()

if __name__ == "__main__":
    main()