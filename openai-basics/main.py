import os
from openai import OpenAI
from dotenv import load_dotenv



def main():
    load_dotenv()

    #read api key from env file.
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Hello! Can you help me with a coding question?"}
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
