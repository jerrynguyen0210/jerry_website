import streamlit as st

from data import PROFILE


def main() -> None:
    st.title("About")
    st.subheader(PROFILE["headline"])
    st.write(PROFILE["summary"])


if __name__ == "__main__":
    main()

