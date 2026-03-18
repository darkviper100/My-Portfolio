import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Chetan Sharma | Portfolio",
    layout="wide",
    page_icon="🎬"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #0d1117;
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #010409;
}

/* Top Bar */

.topbar {
    background: #161b22;
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 10px;
}

/* Title */

.main-title {
    font-size: 34px;
    font-weight: bold;
    color: #58a6ff;
}

/* Card */

.card {
    background: #161b22;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #30363d;
    text-align: center;
}

/* Avatar */

.avatar {
    border-radius: 50%;
    border: 2px solid #58a6ff;
}

</style>
""", unsafe_allow_html=True)

# ---------------- FUNCTIONS ----------------


def show_under_construction(name):

    st.markdown(f"<div class='main-title'>{name}</div>", unsafe_allow_html=True)

    st.warning(f"{name} section under development")

    with st.status("Loading...", expanded=True):

        st.write("Preparing layout")
        time.sleep(0.5)

        st.write("Rendering assets")
        time.sleep(0.5)

        st.write("Almost done")
        time.sleep(0.5)

    st.image(
        "https://via.placeholder.com/700x350.png?text=Coming+Soon",
        use_container_width=True
    )


# ---------------- HOME ----------------


def show_overview():

    st.markdown(
        """
        <div class="topbar">
        <span class="main-title">Chetan Sharma</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1,3])

    with col1:

        st.image(
            "https://i.imgur.com/8Km9tLL.png",
            width=150
        )

    with col2:

        st.write("### Digital Creator")
        st.write("Video Editing • Social Media • Web • Content")

    st.write("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("<div class='card'>🎬 Video Editing</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='card'>📊 Social Media</div>", unsafe_allow_html=True)

    with c3:
        st.markdown("<div class='card'>🌐 Web Skills</div>", unsafe_allow_html=True)


# ---------------- CONNECT ----------------


def show_connect():

    st.markdown("<div class='main-title'>Connect</div>", unsafe_allow_html=True)

    st.link_button("LinkedIn", "https://linkedin.com")

    st.code("workwithchetansharma@gmail.com")


# ---------------- MAIN ----------------


def main():

    with st.sidebar:

        st.image(
            "https://i.imgur.com/8Km9tLL.png",
            width=80
        )

        st.markdown("### Chetan Sharma")
        st.caption("Portfolio Dashboard")

        choice = st.radio(
            "",
            [
                "Overview",
                "Video Editing",
                "Photo Editing",
                "Social Media",
                "Content Writing",
                "Connect"
            ]
        )

        st.markdown("---")
        st.caption("v2.1")

    if choice == "Overview":
        show_overview()

    elif choice == "Video Editing":
        show_under_construction("Video Editing")

    elif choice == "Photo Editing":
        show_under_construction("Photo Editing")

    elif choice == "Social Media":
        show_under_construction("Social Media")

    elif choice == "Content Writing":
        show_under_construction("Content Writing")

    elif choice == "Connect":
        show_connect()


if __name__ == "__main__":
    main()