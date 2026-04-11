import base64
from pathlib import Path

import streamlit as st


def main() -> None:
    pdf_path = Path(__file__).resolve().parents[1] / "docs" / "Jerry_CV.pdf"

    if not pdf_path.exists():
        st.error("Resume PDF not found: docs/Jerry_CV.pdf")
        return

    pdf_base64 = base64.b64encode(pdf_path.read_bytes()).decode("utf-8")
    pdf_viewer = f"""
        <iframe
            src="data:application/pdf;base64,{pdf_base64}"
            width="100%"
            height="1200"
            style="border: none;"
        ></iframe>
    """
    st.markdown(pdf_viewer, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
