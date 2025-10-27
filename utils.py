import google.generativeai as genai
from fastapi import APIRouter
from pydantic import BaseModel
import os

router = APIRouter()

# configure Gemini with your API key
genai.configure(api_key="AIzaSyBkaywgMs7OTBPX204npyTVGgkXKn-gCCM")

class PromptInput(BaseModel):
    prompt: str  # e.g., "I feel stressed today"

@router.post("/recommend")
async def recommend(input_data: PromptInput):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")


        response = model.generate_content(
            f"""
            The user feels: "{input_data.prompt}"
            Suggest 3 music songs (YouTube, Spotify) and 3 ebooks (Google Books or other) ,e audio books and 3 youtube videos
            that match their mood. Return the output in JSON format like:
            {{
              "music": ["song1", "song2", "song3"],
              "ebooks": ["book1", "book2", "book3"],
              "audiobooks": ["abook1", "abook2", "abook3"],
              "videos": ["video11", "video2", "video3"],

            }}
            """
        )

        # Extract the text response safely
        return {"recommendations": response.text}

    except Exception as e:
        return {"error": str(e)}
