import streamlit as st

from data import CONTACT


def main() -> None:
    # Clear chat histories when user is on the Contact page
    for key in ("smart_jerry_messages", "junior_jerry_messages"):
        if key in st.session_state:
            del st.session_state[key]

    st.title("Contact")

    st.write("Feel free to reach out using any of the channels below.")

    email = CONTACT.get("email")
    location = CONTACT.get("location")

    if email:
        st.markdown(f"**Email:** [{email}](mailto:{email})")
    if location:
        st.markdown(f"**Location:** {location}")

    if CONTACT.get("github"):
        st.markdown(f"**GitHub:** {CONTACT['github']}")
    if CONTACT.get("linkedin"):
        st.markdown(f"**LinkedIn:** {CONTACT['linkedin']}")
    if CONTACT.get("website"):
        st.markdown(f"**Website:** {CONTACT['website']}")

    socials = CONTACT.get("socials") or []
    if socials:
        st.subheader("Social links")
        for social in socials:
            st.markdown(f"- [{social['label']}]({social['url']})")


if __name__ == "__main__":
    main()
