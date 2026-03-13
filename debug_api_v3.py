import os
from google import genai
from dotenv import load_dotenv

# Try to find and load .env
env_path = os.path.join(os.getcwd(), '.env')
print(f"Current working directory: {os.getcwd()}")
print(f"Looking for .env at: {env_path}")
print(f"File exists: {os.path.exists(env_path)}")

load_dotenv()

def debug_api():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("!!! ERROR: GEMINI_API_KEY is EMPTY or NOT FOUND in .env !!!")
        return
    
    # Mask key for safety in logs
    masked_key = api_key[:5] + "..." + api_key[-5:] if len(api_key) > 10 else "***"
    print(f"Using API Key: {masked_key}")
    
    try:
        client = genai.Client(api_key=api_key)
        print("Connecting to Gemini API...")
        
        # Test 1: List Models
        print("\nTest 1: Listing models...")
        models = [m.name for m in client.models.list()]
        for m in models:
            print(f"- {m}")
        
        # Test 2: Simple generation
        print("\nTest 2: Basic text generation test...")
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents="Say hello!"
        )
        print(f"Response: {response.text}")
        print("\nSUCCESS: API is working correctly!")
        
    except Exception as e:
        print(f"\n!!! API ERROR !!!")
        print(f"Error Type: {type(e)}")
        print(f"Error Message: {str(e)}")
        if "403" in str(e):
            print("Note: This 403 usually means the key is blocked/leaked or your region is restricted.")
        if "404" in str(e):
            print("Note: This 404 might mean the model name is incorrect for this API version.")

if __name__ == "__main__":
    debug_api()
