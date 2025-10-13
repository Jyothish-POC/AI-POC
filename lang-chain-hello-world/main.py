import os
from dotenv import load_dotenv

def main():
    print("Hello from lang-chain-hello-world!")

    # Load environment variables from .env file
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")
    print(f"OpenAI API Key: {openai_api_key}")
    print(f"Google API Key: {google_api_key}")


if __name__ == "__main__":
    main()
