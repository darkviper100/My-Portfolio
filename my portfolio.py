import streamlit as st
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Chetan Sharma | Creative Portfolio", layout="wide", page_icon="🎬")

# Custom CSS for Sleek Dark Theme & UI Elements
st.markdown("""
    <style>
    .stApp { background-color: #0b0d10; } 
    .stHeading, h1, h2, h3 { color: #ffffff !important; font-family: 'Inter', sans-serif; }
    .stSubheader { color: #00e6ff !important; font-weight: 400; }
    
    /* Profile Picture Styling */
    .pfp-container {
        display: flex;
        justify-content: flex-end;
        padding-top: 10px;
    }
    .pfp-image {
        border-radius: 50%;
        border: 2px solid #00e6ff;
        width: 120px;
        height: 120px;
        object-fit: cover;
    }
    
    /* Portfolio Cards */
    .stCard { 
        background-color: #14161a; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #222;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
col_title, col_pfp = st.columns([4, 1])

with col_title:
    st.title("Chetan Sharma")
    st.subheader("Video Editor | Social Media Strategist | Content Writer")

with col_pfp:
    # Path for your PFP (Make sure pfp.jpg is in the same folder)
    pfp_path = "pfp.jpg" 
    if os.path.exists(pfp_path):
        st.image(pfp_path, width=120)
    else:
        st.markdown('<div class="pfp-container"><img src="https://via.placeholder.com/120?text=PFP" class="pfp-image"></div>', unsafe_allow_html=True)

st.markdown("---")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.write("### 🧭 Navigation")
    choice = st.radio("Go to", [
        "Overview", 
        "🎬 Video Editing", 
        "📸 Photo Editing (Slider)", 
        "📊 Social Media Mgmt", 
        "✍️ Content Writing",
        "🌐 Connect with Me"
    ])

# --- 1. OVERVIEW ---
if choice == "Overview":
    st.title("🚀 Professional Summary")
    st.write("""
    I am a results-oriented creator specializing in high-retention video content and data-driven social media strategies. 
    By blending technical proficiency in tools like **DaVinci Resolve** with a logical mindset, 
    I help brands and creators scale their digital presence effectively.
    """)
    st.info("Currently open for Remote Roles & Freelance Projects.")
    st.write("### 🛠️ Tech Stack")
    st.code("DaVinci Resolve | VN Editor | Canva | Python | OSINT Basics")

# --- 2. VIDEO EDITING ---
elif choice == "🎬 Video Editing":
    st.title("🎬 Video Editing Showcase")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Project 1: Gaming/High-Energy")
        # st.video("videos/gaming_sample.mp4") # Un-comment and add path
        st.image("https://via.placeholder.com/800x450.png?text=Gaming+Edit+Thumbnail", use_container_width=True)
    with col2:
        st.write("### Project 2: Brand/Corporate")
        # st.video("videos/brand_sample.mp4") # Un-comment and add path
        st.image("https://via.placeholder.com/800x450.png?text=Brand+Promo+Thumbnail", use_container_width=True)

# --- 3. PHOTO EDITING (SLIDER) ---
elif choice == "📸 Photo Editing (Slider)":
    st.title("📸 Visual Transformation Proof")
    st.write("Drag the slider to see my editing process in action.")
    
    # Files needed: before.jpg and after.jpg
    # Using a workaround for Streamlit Slider if files don't exist
    st.image("https://via.placeholder.com/1200x600.png?text=Photo+Editing+Before+After+Proof", use_container_width=True)
    st.caption("I specialize in Color Grading, Subject Isolation, and Lighting Correction.")

# --- 4. SOCIAL MEDIA MGMT ---
elif choice == "📊 Social Media Mgmt":
    st.title("📊 Strategy & Analytics")
    st.write("### Data-Driven Organic Growth")
    st.image("https://via.placeholder.com/800x400.png?text=Strategy+Calendar+Preview", use_container_width=True)
    st.write("I provide full-cycle management including content planning, posting, and performance auditing.")

# --- 5. CONTENT WRITING ---
elif choice == "✍️ Content Writing":
    st.title("✍️ Content Showcase")
    st.write("### Articles & Copywriting")
    st.code("""
    Headline: Why Video is the #1 Growth Tool in 2026
    Content: Research shows that 90% of consumers prefer...
    [Click to read full article]
    """)

# --- 6. CONNECT WITH ME ---
elif choice == "🌐 Connect with Me":
    st.title("🌐 Let's Collaborate")
    st.write("### My Official Channels")
    
    # Replace these with your actual links
    st.markdown("- [🔗 LinkedIn (Process Underway)](#)")
    st.markdown("- [🎬 YouTube (Portfolio Channel)](#)")
    st.markdown("- [📸 Instagram (Creative Work)](#)")
    
    st.write("---")
    st.subheader("📩 Contact Directly")
    st.write("Email: workwithchetansharma@gmail.com")
    if st.button("Celebrate Connection! 🎉"):
        st.balloons()