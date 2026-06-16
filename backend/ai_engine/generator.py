from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(env_path)

print("API KEY =", os.getenv("GEMINI_API_KEY"))

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_backlog(prompt, requirement):

    full_prompt = f"""
    {prompt}

    Requirement Document:

    {requirement}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text