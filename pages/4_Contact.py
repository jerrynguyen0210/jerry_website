import streamlit as st

from data import CONTACT


def main() -> None:
    st.title("Contact")

    st.write("Feel free to reach out using any of the channels below.")

    st.markdown(f"**Email:** [{CONTACT['email']}](mailto:{CONTACT['email']})")
    st.markdown(f"**Location:** {CONTACT['location']}")

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

