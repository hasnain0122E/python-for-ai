import os
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

api_key = os.environ.get("OPENAI_API_KEY")
database_url = os.environ.get("DATABASE_URL")

print(f"API Key: {api_key}")
print(f"Database URL: {database_url}")
