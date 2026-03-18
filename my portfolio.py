import streamlit as st
import time

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Chetan Sharma | Portfolio",
    layout="wide",
    page_icon="🎬"
)

# --- CUSTOM CSS (Professional Dark UI) ---
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #0b0d10, #111827);
    color: white;
}

.main-title {
    color: #00e6ff;
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    color: #9ca3af;
    font-size: 18px;
}

.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #1f2937;
    margin-bottom: 15px;
}

.sidebar-title {
    color: #00e6ff;
    font-size: 22px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ---------- FUNCTIONS ----------

def show_under_construction(section_name):

    st.markdown(f"<div class='main-title'>{section_name}</div>", unsafe_allow_html=True)
    st.write("---")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.warning(f"🚧 {section_name} section under development")

        with st.status("Rendering assets...", expanded=True):
            st.write("Loading modules...")
            time.sleep(0.7)
            st.write("Applying UI polish...")
            time.sleep(0.7)
            st.write("Finalizing layout...")
            time.sleep(0.7)

        st.info("Elite quality work in progress 🔥")

        st.image(
            "https://via.placeholder.com/700x350.png?text=Coming+Soon",
            use_container_width=True
        )


# ---------- HOME ----------

def show_overview():

    st.markdown("<div class='main-title'>Chetan Sharma</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Digital Creator • Video Editor • Web Learner</div>", unsafe_allow_html=True)

    st.write("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>🎬 Video Editing<br>High retention edits</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>📊 Social Media<br>Content strategy</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>🌐 Web Skills<br>HTML CSS JS</div>", unsafe_allow_html=True)

    st.write("---")

    st.success("Portfolio Dashboard Live")


# ---------- CONNECT ----------

def show_connect():

    st.markdown("<div class='main-title'>Connect With Me</div>", unsafe_allow_html=True)

    st.write("Available for freelance & job work")

    st.link_button("LinkedIn", "https://linkedin.com")

    st.code("workwithchetansharma@gmail.com")


# ---------- MAIN ----------

def main():

    with st.sidebar:

        st.markdown("<div class='sidebar-title'>📂 Portfolio Menu</div>", unsafe_allow_html=True)

        choice = st.radio(
            "",
            [
                "🏠 Overview",
                "🎬 Video Editing",
                "📸 Photo Editing",
                "📊 Social Media",
                "✍️ Content Writing",
                "🌐 Connect"
            ]
        )

        st.markdown("---")
        st.caption("v2.0 | Built with Streamlit")

    if choice == "🏠 Overview":
        show_overview()

    elif choice == "🎬 Video Editing":
        show_under_construction("Video Editing")

    elif choice == "📸 Photo Editing":
        show_under_construction("Photo Editing")

    elif choice == "📊 Social Media":
        show_under_construction("Social Media")

    elif choice == "✍️ Content Writing":
        show_under_construction("Content Writing")

    elif choice == "🌐 Connect":
        show_connect()


if __name__ == "__main__":
    main()