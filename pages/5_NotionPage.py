import streamlit as st
from pathlib import Path


NOTION_PAGE_URL = "https://www.notion.so/To-do-List-455e070e52194ce7a65525d0406b9222?source=copy_link"
NOTION_SCREENSHOT_PATH = "assets/notion_preview.png"


def main() -> None:
    st.title("Notion Page")
    st.write(
        "Notion does not allow this public page to be embedded inside other websites, "
        "so it cannot be displayed directly here. "
        "You can open it in Notion using the button below."
    )

    if Path(NOTION_SCREENSHOT_PATH).exists():
        st.image(NOTION_SCREENSHOT_PATH, caption="Notion To-do List (static preview)")
    else:
        st.info("Add a screenshot at `assets/notion_preview.png` to show a static preview.")

    st.link_button("Open in Notion", NOTION_PAGE_URL)


if __name__ == "__main__":
    main()
