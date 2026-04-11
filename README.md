# Jerry Website

A personal portfolio website built with [Streamlit](https://streamlit.io/). The app currently includes a landing page, a resume viewer, and project cards, with most content managed from a single data file.

## Tech Stack

- Python 3.12
- Streamlit 1.54
- Docker

## Project Structure

```text
.
├── app.py                  # Main Streamlit app and navigation
├── data.py                 # Centralized profile, projects, experience, skills, contact data
├── pages/
│   ├── 2_Projects.py       # Projects listing page
│   └── 3_Resume.py         # Resume page
├── docs/my_summary.txt     # Summary text shown on the homepage
├── docs/Jerry_CV.pdf       # Resume PDF embedded on the resume page
├── assets/                 # Images and static assets
├── requirements.txt
└── Dockerfile
```

## Features

- Multi-page Streamlit portfolio layout
- Centralized content management in `data.py`
- Summary text loaded from `docs/my_summary.txt`
- Project cards with GitHub and live demo links
- Embedded PDF resume page
- Dockerized deployment for consistent hosting

## Run Locally

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
streamlit run app.py
```

The app runs on `http://localhost:8501` by default.

## Docker

Build the image:

```bash
docker build -t jerrynguyen0210/jerry_web:latest .
```

Tag the image:

```bash
docker tag jerry-website:latest jerrynguyen0210/jerry_web:latest
```

Push the image:

```bash
docker push jerrynguyen0210/jerry_web:latest
```

Pull the image:

```bash
docker pull jerrynguyen0210/jerry_web:latest
```

Run the container:

```bash
docker run -d -p 8501:8501 jerrynguyen0210/jerry_web:latest
```

If you are building specifically for Raspberry Pi 5 or another ARM64 target, make sure you build for `linux/arm64`.

## Content Customization

Most site content can be updated without changing layout code:

- Edit `PROFILE`, `PROJECTS`, `EXPERIENCE`, `EDUCATION`, `SKILLS`, and `CONTACT` in `data.py`
- Update the personal summary in `docs/my_summary.txt`
- Replace `docs/Jerry_CV.pdf` with your current resume

## Navigation Notes

The current app navigation in `app.py` exposes these sections:

- Introduction
- Resume
- Projects

## Deployment Notes

- The container listens on port `8501`
- The Docker healthcheck uses Streamlit's `/_stcore/health` endpoint
- `Dockerfile` is configured for headless Streamlit execution

## Next Improvements

- Replace placeholder profile data in `data.py`
- Add more projects and resume entries
- Add CI or deployment automation for image publishing
