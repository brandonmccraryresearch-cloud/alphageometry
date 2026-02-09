# llm_client.py
import os
from google import genai
from google.genai import types

class GeminiPhysicsClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")
        self.client = genai.Client(api_key=self.api_key)
        self.model_id = "gemini-3-pro-preview"

        with open("system_instruction.txt", "r") as f:
            self.system_instruction = f.read()

    def generate_reconstruction(self, prompt):
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt),
                ],
            ),
        ]
        tools = [
            types.Tool(url_context=types.UrlContext()),
            types.Tool(code_execution=types.ToolCodeExecution),
            types.Tool(google_search=types.GoogleSearch()),
        ]
        generate_content_config = types.GenerateContentConfig(
            temperature=0.97,
            top_p=0.97,
            thinking_config=types.ThinkingConfig(
                thinking_level="HIGH",
            ),
            media_resolution="MEDIA_RESOLUTION_HIGH",
            tools=tools,
            system_instruction=[
                types.Part.from_text(text=self.system_instruction),
            ],
        )

        response = self.client.models.generate_content(
            model=self.model_id,
            contents=contents,
            config=generate_content_config,
        )
        return response.text

if __name__ == "__main__":
    # Test client
    try:
        client = GeminiPhysicsClient()
        print("Client initialized successfully.")
    except Exception as e:
        print(f"Error: {e}")
