from dotenv import load_dotenv
import os
from mistralai import Mistral
import base64

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None


def get_informations_from_image(image_path):
    load_dotenv()
    api_key = os.environ["MISTRAL_API_KEY"]
    # Getting the base64 string
    base64_image = encode_image(image_path)

    # Retrieve the API key from environment variables


    # Specify model
    model = "pixtral-12b-2409"

    # Initialize the Mistral client
    client = Mistral(api_key=api_key)

    # Define the messages for the chat
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """Extract the following details from a given image of receipt (your answer must be in short JSON object."):
                                1. Reservation Date
                                2. Company Name
                                3. Amount incl. VAT
                                4. Currency"""},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}" 
                }
            ]
        }
    ]

    # Get the chat response
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
        response_format = {"type": "json_object"},
    )

    # Print the content of the response
    return chat_response.choices[0].message.content