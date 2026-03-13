import streamlit as st

from data import EXPERIENCE, EDUCATION, SKILLS


def main() -> None:
    # Clear chat histories when user is on the Resume page
    for key in ("smart_jerry_messages", "junior_jerry_messages"):
        if key in st.session_state:
            del st.session_state[key]
    st.title("Resume")

    st.subheader("Experience")
    for role in EXPERIENCE:
        st.markdown(f"**{role['role']}** · {role['company']} · {role['location']}")
        st.caption(f"{role['start']} – {role['end']}")
        for bullet in role.get("bullets", []):
            st.markdown(f"- {bullet}")
        if tech := role.get("tech"):
            st.caption("Tech: " + ", ".join(tech))
        st.markdown("---")

    st.subheader("Education")
    for edu in EDUCATION:
        st.markdown(f"**{edu['degree']} {edu['field']}** · {edu['school']}")
        st.caption(f"{edu['location']} · {edu['start']} – {edu['end']}")

    st.subheader("Skills")
    cols = st.columns(len(SKILLS))
    for col, (category, items) in zip(cols, SKILLS.items()):
        with col:
            st.markdown(f"**{category}**")
            st.write(", ".join(items))
 
if __name__ == "__main__":
    main()

