import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def list_models():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found in .env")
        return
    
    try:
        client = genai.Client(api_key=api_key)
        print("Checking models...")
        # Try to list models to see what we have access to
        for model in client.models.list():
            print(f"- {model.name}")
            # print(f"  Methods: {model.supported_generation_methods}")
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_models()
