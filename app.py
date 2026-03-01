import streamlit as st
from pathlib import Path

from data import PROFILE, get_summary, PROJECTS, SKILLS, CONTACT


st.set_page_config(
    page_title="Jerry - Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)


def _home() -> None:
    # Header: name, role, value statement
    st.title(PROFILE["name"])
    st.subheader(PROFILE["headline"])
    if get_summary():
        st.write(get_summary())

    # Hero: profile photo + quick intro
    st.markdown("---")
    left, right = st.columns([1, 2])

    with left:
        profile_path = Path("assets/profile.jpg")
        if profile_path.exists():
            st.image(str(profile_path), use_container_width=True)
        else:
            st.info("Add a profile photo at `assets/profile.jpg`.")

    with right:
        st.markdown("### Quick intro")
        st.write(
            "This is a sample hero introduction. Replace it with a short paragraph "
            "about who you are, what you work on, and what you're looking for."
        )

        # Primary call-to-action buttons
        st.markdown("### Connect")
        btn_cols = st.columns(4)
        with btn_cols[0]:
            if CONTACT.get("github"):
                st.link_button("GitHub", CONTACT["github"])
        with btn_cols[1]:
            if CONTACT.get("linkedin"):
                st.link_button("LinkedIn", CONTACT["linkedin"])
        with btn_cols[2]:
            if CONTACT.get("email"):
                st.link_button("Email", f"mailto:{CONTACT['email']}")
        with btn_cols[3]:
            resume_url = CONTACT.get("resume_url")
            if resume_url:
                st.link_button("Resume", resume_url)

    # Featured projects preview
    st.markdown("---")
    st.subheader("Featured projects")
    featured = [p for p in PROJECTS if p.get("featured")]
    featured = sorted(featured, key=lambda p: p.get("year", 0), reverse=True)[:3]

    if not featured:
        st.write("Add featured projects in `data.py` to showcase them here.")
    else:
        for project in featured:
            with st.container(border=True):
                st.markdown(f"**{project['name']}**")
                if project.get("tagline"):
                    st.caption(project["tagline"])
                st.write(project["description"])

                meta_cols = st.columns(3)
                with meta_cols[0]:
                    if tech := project.get("tech"):
                        st.caption("Tech: " + ", ".join(tech))
                with meta_cols[1]:
                    if repo := project.get("repo_url"):
                        st.link_button("GitHub", repo)
                with meta_cols[2]:
                    if demo := project.get("demo_url"):
                        st.link_button("Live demo", demo)

    # Skills highlights
    st.markdown("---")
    st.subheader("Skills highlights")
    categories = list(SKILLS.items())[:3]
    cols = st.columns(len(categories) or 1)
    for col, (category, items) in zip(cols, categories):
        with col:
            st.markdown(f"**{category}**")
            st.write(", ".join(items))

    # Footer
    st.markdown("---")
    footer_cols = st.columns(3)
    with footer_cols[0]:
        st.caption(
            f"{CONTACT.get('location', '')} · {CONTACT.get('timezone', '')}".strip(" ·")
        )
    with footer_cols[1]:
        if CONTACT.get("email"):
            st.caption(CONTACT["email"])
    with footer_cols[2]:
        links = []
        if CONTACT.get("github"):
            links.append("[GitHub](" + CONTACT["github"] + ")")
        if CONTACT.get("linkedin"):
            links.append("[LinkedIn](" + CONTACT["linkedin"] + ")")
        if CONTACT.get("website"):
            links.append("[Website](" + CONTACT["website"] + ")")
        if links:
            st.caption(" · ".join(links))


if __name__ == "__main__":
    home_page = st.Page(_home, title="Home", default=True)
    about_page = st.Page("pages/1_About.py", title="About")
    projects_page = st.Page("pages/2_Projects.py", title="Projects")
    demo_01_page = st.Page("pages/2_Projects_demo_01.py", title="Raspberry Pi 5 LLM Chat")
    demo_page = st.Page("pages/2_Projects_demo_02.py", title="Ollama Chatbot")
    resume_page = st.Page("pages/3_Resume.py", title="Resume")
    contact_page = st.Page("pages/4_Contact.py", title="Contact")
    notion_page = st.Page("pages/5_NotionPage.py", title="Notion Page")

    pg = st.navigation(
        {
            "": [home_page, about_page, resume_page, contact_page, notion_page],
            "Projects": [projects_page, demo_01_page, demo_page],
        }
    )
    pg.run()

