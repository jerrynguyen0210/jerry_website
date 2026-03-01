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
        "slug": "sample-portfolio",
        "name": "Personal Portfolio",
        "tagline": "A modern Streamlit-based personal site.",
        "description": (
            "Describe what this project does, why you built it, and what makes it "
            "interesting or technically noteworthy."
        ),
        "tech": ["Python", "Streamlit"],
        "highlights": [
            "Responsive multi-page layout with custom theming.",
            "Centralized content configuration in data.py.",
        ],
        "repo_url": "",
        "demo_url": "",
        "year": 2025,
        "featured": True,
    },
    # Add more projects here
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
