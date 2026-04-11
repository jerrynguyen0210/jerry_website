import streamlit as st
import streamlit.components.v1 as components
from html import escape
from textwrap import dedent

from data import PROFILE, get_summary


st.set_page_config(
    page_title="Jerry - Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)


def _home() -> None:
    summary = get_summary()
    intro_text = summary or "Building dependable software experiences with clarity, care, and a product mindset."
    paragraphs = [p.strip() for p in intro_text.split("\n\n") if p.strip()]
    summary_html = "".join(f'<p class="about-body">{escape(p)}</p>' for p in paragraphs)

    components.html(
        dedent(
            f"""
        <style>
            body {{
                margin: 0;
                background: transparent;
                font-family: "Trebuchet MS", "Segoe UI", sans-serif;
            }}
            .stApp {{
                background: linear-gradient(135deg, #e9e3de 0%, #f5f1ec 100%);
            }}
            .block-container {{
                padding-top: 2rem;
                padding-bottom: 2rem;
            }}
            .about-wrap {{
                position: relative;
                max-width: 980px;
                margin: 0 auto;
                padding-left: 4.5rem;
            }}
            .about-card {{
                background:
                    linear-gradient(135deg, rgba(255, 255, 255, 0.92), rgba(245, 240, 236, 0.94)),
                    radial-gradient(circle at right center, rgba(0, 0, 0, 0.04), transparent 30%);
                border-radius: 4px;
                padding: 2.2rem 2.4rem 2.6rem 2.4rem;
                box-shadow: 0 18px 40px rgba(70, 48, 34, 0.12);
                overflow: hidden;
                position: relative;
            }}
            .about-card::after {{
                content: '';
                position: absolute;
                inset: 0;
                background:
                    radial-gradient(circle at 88% 36%, rgba(0, 0, 0, 0.06), transparent 24%),
                    radial-gradient(circle at 80% 48%, rgba(0, 0, 0, 0.045), transparent 18%),
                    radial-gradient(circle at 92% 62%, rgba(0, 0, 0, 0.035), transparent 18%);
                opacity: 0.55;
                pointer-events: none;
            }}
            .about-ribbon {{
                position: absolute;
                left: 0;
                top: 0.9rem;
                width: 2.2rem;
                height: 9rem;
                background: linear-gradient(180deg, #7d1600 0%, #a02605 100%);
                color: #fff4ea;
                display: flex;
                align-items: center;
                justify-content: center;
                writing-mode: vertical-rl;
                transform: rotate(180deg);
                font-size: 1.15rem;
                font-weight: 700;
                letter-spacing: 0.04rem;
                box-shadow: 0 10px 18px rgba(91, 24, 7, 0.22);
            }}
            .about-ribbon::after {{
                content: '';
                position: absolute;
                bottom: -14px;
                left: 0;
                border-left: 18px solid #5f0d00;
                border-top: 14px solid transparent;
            }}
            .about-title {{
                font-family: Georgia, "Times New Roman", serif;
                color: #050505;
                font-size: 4rem;
                line-height: 1;
                font-weight: 700;
                letter-spacing: -0.05em;
                margin: 0 0 1rem 0;
            }}
            .about-lead {{
                max-width: 700px;
                color: #0d4d57;
                font-family: Georgia, "Times New Roman", serif;
                font-size: 1.85rem;
                line-height: 1.2;
                font-weight: 700;
                margin: 0 0 2rem 0;
            }}
            .about-body {{
                max-width: 720px;
                color: #111111;
                font-size: 1.08rem;
                line-height: 1.9;
                margin: 0;
            }}
            .about-body + .about-body {{
                margin-top: 1.4rem;
            }}
            @media (max-width: 900px) {{
                .about-wrap {{
                    padding-left: 0;
                }}
                .about-ribbon {{
                    position: relative;
                    top: 0;
                    margin-bottom: 1rem;
                    height: 2.2rem;
                    width: 8rem;
                    writing-mode: horizontal-tb;
                    transform: none;
                }}
                .about-ribbon::after {{
                    display: none;
                }}
                .about-card {{
                    padding: 1.6rem 1.3rem 1.9rem 1.3rem;
                }}
                .about-title {{
                    font-size: 2.8rem;
                }}
                .about-lead {{
                    font-size: 1.4rem;
                }}
            }}
        </style>
        <section class="about-wrap">
            <div class="about-ribbon">About</div>
            <div class="about-card">
                <h1 class="about-title">Hi I&apos;m {PROFILE["name"].split()[0]}</h1>
                <p class="about-lead">{PROFILE["headline"]}</p>
                {summary_html}
            </div>
        </section>
    """
        ),
        height=760,
        scrolling=False,
    )


if __name__ == "__main__":
    home_page = st.Page(_home, title="Introduction", default=True, icon="🏠")
    resume_page = st.Page("pages/3_Resume.py", title="Resume", icon="📄")
    projects_page = st.Page("pages/2_Projects.py", title="Projects", icon="📁")

    pg = st.navigation(
        {
            "Home": [home_page],
            "Personal Profile": [resume_page],
            "Projects": [projects_page],
        }
    )
    pg.run()
