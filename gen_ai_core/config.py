from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")

GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
OPEN_ROUTER_BASE_URL = os.getenv("OPEN_ROUTER_BASE_URL")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

if not OPEN_ROUTER_API_KEY:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env")