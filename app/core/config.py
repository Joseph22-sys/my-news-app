from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


DATABASE_URL = "sqlite:///./news.db"

# Base directory (root of the project)
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths for templates & static files
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"