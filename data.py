from __future__ import annotations

from pathlib import Path
from typing import TypedDict, List, Dict, Optional


def _load_summary() -> str:
    path = Path(__file__).parent / "docs/my_summary.txt"
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return ""


def get_summary() -> str:
    """Load summary from my_summary.txt (called at render time so edits show without restart)."""
    return _load_summary() or (
        "Short professional summary about your background, focus areas, and what "
        "you enjoy building. Update this text in my_summary.txt."
    )


class SocialLink(TypedDict, total=False):
    label: str
    url: str
    icon: str


class Project(TypedDict, total=False):
    slug: str
    name: str
    tagline: str
    description: str
    tech: List[str]
    highlights: List[str]
    repo_url: Optional[str]
    demo_url: Optional[str]
    year: Optional[int]
    featured: bool


class Experience(TypedDict, total=False):
    company: str
    role: str
    location: str
    start: str
    end: str
    bullets: List[str]
    tech: List[str]


class Education(TypedDict, total=False):
    school: str
    degree: str
    field: str
    location: str
    start: str
    end: str


class ContactInfo(TypedDict, total=False):
    email: str
    location: str
    github: str
    linkedin: str
    website: str
    socials: List[SocialLink]
    timezone: str
    resume_url: str


class Profile(TypedDict, total=False):
    name: str
    headline: str
    summary: str
    contact: ContactInfo


PROFILE: Profile = {
    "name": "Jerry YourLastName",
    "headline": "Software Engineer",
    "summary": _load_summary() or (
        "Short professional summary about your background, focus areas, and what "
        "you enjoy building. Update this text in my_summary.txt."
    ),
    "contact": {
        "email": "you@example.com",
        "location": "City, Country",
        "github": "https://github.com/your-handle",
        "linkedin": "https://www.linkedin.com/in/your-handle/",
        "website": "https://jerryitdev.com",
        "timezone": "Your Timezone",
        "resume_url": "",
        "socials": [
            {
                "label": "GitHub",
                "url": "https://github.com/your-handle",
                "icon": "github",
            },
            {
                "label": "LinkedIn",
                "url": "https://www.linkedin.com/in/your-handle/",
                "icon": "linkedin",
            },
        ],
    },
}


PROJECTS: List[Project] = [
    {
        "slug": "mobile-selling-chatbot-vietnamese",
        "name": "Mobile Selling Chatbot Vietnamese",
        "tagline": "A Vietnamese AI chatbot that recommends mobile phones using a RAG pipeline.",
        "description": (
            "An AI-powered mobile phone selling chatbot for the Vietnamese market. "
            "Users can browse phones by brand or budget, ask about features such "
            "as battery life, camera quality, and performance, and receive tailored "
            "recommendations generated from retrieved product data."
        ),
        "tech": [
            "Python",
            "Streamlit",
            "FastAPI",
            "PostgreSQL",
            "Redis",
            "Qdrant",
            "Docker",
            "Claude",
        ],
        "highlights": [
            "Built a Retrieval-Augmented Generation workflow that searches product embeddings before generating answers.",
            "Combined a Streamlit frontend with a FastAPI backend for chat interactions and API-driven architecture.",
            "Used PostgreSQL for conversation history, Redis for session caching, and Qdrant for vector search.",
        ],
        "repo_url": "https://github.com/jerrynguyen0210/Mobile_Selling_Chatbot_Vietnamese",
        "demo_url": "https://app01.jerryitdev.com/",
        "year": 2026,
        "featured": True,
    },
    {
        "slug": "chatbot-desktop-app",
        "name": "Chatbot Desktop App",
        "tagline": "A Qt desktop chat client with a FastAPI backend and optional RAG workflows.",
        "description": (
            "A desktop chatbot application built with a C++ Qt interface and a "
            "Python FastAPI server. The app supports multiple LLM providers, lets "
            "users upload and index documents for retrieval-augmented generation, "
            "and routes chat requests through a backend API designed for local or "
            "cloud-based model access."
        ),
        "tech": [
            "C++",
            "Qt",
            "Python",
            "FastAPI",
            "LangChain",
            "Qdrant",
        ],
        "highlights": [
            "Built a desktop chat interface with agent switching across OpenAI, Anthropic, Google, and local model providers.",
            "Implemented RAG session management with file upload, indexing, retrieval, and session activation from the app.",
            "Separated the system into a Qt frontend and FastAPI backend for cleaner API-driven development.",
        ],
        "repo_url": "https://github.com/jerrynguyen0210/Chatbot_Desktop_App",
        "demo_url": None,
        "year": 2026,
        "featured": True,
    },
]


EXPERIENCE: List[Experience] = [
    {
        "company": "Your Company",
        "role": "Your Role",
        "location": "City, Country",
        "start": "YYYY",
        "end": "Present",
        "bullets": [
            "Key achievement or responsibility you want to highlight.",
            "Another impact-focused bullet with metrics if possible.",
        ],
        "tech": ["Python", "Streamlit"],
    },
    # Add more roles here
]


EDUCATION: List[Education] = [
    {
        "school": "Your University",
        "degree": "BSc",
        "field": "Computer Science",
        "location": "City, Country",
        "start": "YYYY",
        "end": "YYYY",
    },
]


SKILLS: Dict[str, List[str]] = {
    "Languages": ["Python", "TypeScript", "SQL"],
    "Frameworks": ["Streamlit", "FastAPI"],
    "Tools": ["Git", "Docker"],
}


CONTACT: ContactInfo = PROFILE["contact"]
