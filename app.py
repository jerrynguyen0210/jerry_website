import streamlit as st
import base64
from pathlib import Path

from data import PROFILE, get_summary, PROJECTS, SKILLS, CONTACT


st.set_page_config(
    page_title="Jerry - Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)


def _home() -> None:
    # Background image

    # Header: name, role, value statement
    summary_html = f"<p style='color: #e0e0e0; font-size: 1rem; margin: 8px 0 0 0;'>{get_summary()}</p>" if get_summary() else ""
    st.markdown(f"""
        <div style="
            background-color: rgba(0, 0, 0, 0.55);
            border-radius: 12px;
            padding: 28px 36px;
            margin-bottom: 16px;
        ">
            <h1 style="color: #ffffff; margin: 0 0 6px 0;">{PROFILE["name"]}</h1>
            <h3 style="color: #f0c070; margin: 0;">{PROFILE["headline"]}</h3>
            {summary_html}
        </div>
    """, unsafe_allow_html=True)

    # Quote card
    st.markdown("""
        <div style="
            background-color: rgba(90, 40, 50, 0.6);
            border-radius: 12px;
            padding: 20px 20px;
            margin: 0 0;
        ">
            <div style="font-size: 48px; color: #a8c5b5; line-height: 1; margin-bottom: 10px;">"</div>
            <p style="
                color: white;
                font-size: 1.3rem;
                font-weight: 600;
                line-height: 1.6;
                margin: 0 0 0 0;
            ">One's friends are that part of the human race with which one can be human.</p>
            <p style="color: #6dbf9e; font-weight: 600; margin: 0;">George Santayana</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    home_page = st.Page(_home, title="Introduction", default=True, icon="🏠")

    resume_page = st.Page("pages/3_Resume.py", title="Resume", icon="📄")
    contact_page = st.Page("pages/4_Contact.py", title="Contact", icon="📧")
    notion_page = st.Page("pages/5_NotionPage.py", title="Notion Page", icon="📝")

    projects_page = st.Page("pages/2_Projects.py", title="Projects", icon="📁")
    # demo_01_page = st.Page("pages/2_Project_Young_Jerry.py", title="Junior Jerry LLM Chat", icon="🤖")
    # demo_page = st.Page("pages/2_Project_Smart_Jerry.py", title="Smart Jerry Chatbot", icon="💬")

    pg = st.navigation(
        {
            "Home": [home_page],
            "Personal Profile": [resume_page, contact_page, notion_page],
            # "Projects": [projects_page, demo_01_page, demo_page],
            "Projects": [projects_page],
        }
    )
    pg.run()

