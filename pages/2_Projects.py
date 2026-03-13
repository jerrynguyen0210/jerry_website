import streamlit as st

from data import PROJECTS


def main() -> None:
    # Clear chat histories when user is on the generic Projects page
    for key in ("smart_jerry_messages", "junior_jerry_messages"):
        if key in st.session_state:
            del st.session_state[key]

    st.title("Projects")

    for project in PROJECTS:
        with st.container(border=True):
            st.subheader(project["name"])
            if project.get("tagline"):
                st.caption(project["tagline"])
            st.write(project["description"])

            cols = st.columns(3)
            with cols[0]:
                if tech := project.get("tech"):
                    st.markdown("**Tech**")
                    st.write(", ".join(tech))
            with cols[1]:
                if repo := project.get("repo_url"):
                    st.markdown("**Code**")
                    st.link_button("GitHub", repo)
            with cols[2]:
                if demo := project.get("demo_url"):
                    st.markdown("**Demo**")
                    st.link_button("Live demo", demo)


if __name__ == "__main__":
    main()

