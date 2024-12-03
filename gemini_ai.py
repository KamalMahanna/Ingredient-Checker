import os
from typing import Optional
from dotenv import load_dotenv

import google.generativeai as genai
from PIL import Image


class IngredientExtractor:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = None

    def configure_model(self) -> None:
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def extract_ingredients(self, image_path: str) -> Optional[str]:
        if not os.path.isfile(image_path):
            print(f"Error: The file {image_path} does not exist.")
            return None

        if not self.model:
            self.configure_model()

        try:
            with Image.open(image_path) as image:
                prompt = self._create_prompt()
                response = self.model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            return None

    @staticmethod
    def _create_prompt() -> str:
        return """
        Act as a food expert.
        Get all the ingredients from this image if any,
        if not found then give not found any,
        now for each ingredient check if it is safe or not,
        sort them by safe and unsafe, also how it is safe and if unsafe then why
        Do not add comments or additional information

        Your output should be in following markdown example format:
        ### Unsafe ingredients:
        - **Ingredient 1**  <br>  Health Benefits of ingredient 1
        - **Ingredient 2**  <br>  Health Benefits of ingredient 2
        ...
        ### Safe ingredients:
        - **Ingredient 3**  <br>  Health risk of ingredient 3
        - **Ingredient 4**  <br>  Health risk of ingredient 4

        ### Comments:
        Add some comment if it is safe or unsafe
        """


def extract_ingredients_with_gemini(image_path: str) -> Optional[str]:
    extractor = IngredientExtractor()
    return extractor.extract_ingredients(image_path)
