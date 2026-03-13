import streamlit as st
import html

from data import PROFILE, get_summary


def main() -> None:
    # Visiting this non-chat page clears any chat histories
    for key in ("smart_jerry_messages", "junior_jerry_messages"):
        if key in st.session_state:
            del st.session_state[key]

    # Custom layout inspired by the provided About Me design
    st.markdown(
        """
        <style>
        .stApp {
            background: radial-gradient(circle at top left, #e7f9e7 0, #d4f2d4 45%, #bde6bd 100%);
        }

        .about-wrapper {
            padding: 0.5rem 0;
        }

        .about-layout {
            display: flex;
            gap: 3rem;
            align-items: stretch;
        }

        .about-right {
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 1.25rem;
        }

        .about-name {
            font-size: 1.1rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #555;
        }

        .about-title {
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: 0.18em;
        }

        .about-title span {
            color: #c39a84;
        }

        .about-pill {
            display: inline-block;
            width: fit-content;
            padding: 0.5rem 1.5rem;
            border-radius: 999px;
            background: #c39a84;
            color: white;
            font-size: 0.9rem;
            box-sizing: border-box;
            max-width: 100%;
            overflow-wrap: break-word;
            word-break: break-all;
            text-align: center;
            line-height: 1.4;
        }

        .about-body {
            font-size: 1rem;
            line-height: 1.8;
            color: #444;
        }

        @media (max-width: 900px) {
            .about-layout {
                flex-direction: column;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    website = PROFILE.get("contact", {}).get("website") or "jerryitdev.com"

    st.markdown('<div class="about-wrapper">', unsafe_allow_html=True)

    col_img, col_text = st.columns([2, 8])

    with col_img:
        # Replace the path below with the final location of your About image
        st.image(
            "assets/about_me.png",
            use_container_width=True,
        )

    with col_text:
        st.markdown(
            f"""
            <div class="about-layout">
              <div class="about-right">
                <div class="about-name">{PROFILE.get("name", "")}</div>
                <div class="about-title">ABOUT <span>ME</span></div>
                <div class="about-pill">{website}</div>
                <p class="about-body">
                  {html.escape(get_summary()).replace(chr(10), "<br>")}
                </p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
