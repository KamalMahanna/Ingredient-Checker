"""
Module for extracting and analyzing ingredients from images using Google's Gemini AI.
"""

import os
from typing import Optional

import streamlit as st
import google.generativeai as genai
from PIL import Image


class IngredientExtractor:
    """Handles the extraction and analysis of ingredients from images."""

    def __init__(self) -> None:
        """Initialize the extractor with API key from Streamlit secrets."""
        self.api_key: str = st.secrets["GOOGLE_API_KEY"]
        self.model = None

    def configure_model(self) -> None:
        """Configure the Gemini model with API key."""
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def extract_ingredients(self, image_path: str) -> Optional[str]:
        """
        Extract ingredients from the image and analyze them.

        Args:
            image_path: Path to the image file

        Returns:
            Optional[str]: Analysis results or None if extraction fails
        """
        if not os.path.isfile(image_path):
            st.error(f"Error: The file {image_path} does not exist.")
            return None

        try:
            if not self.model:
                self.configure_model()

            with Image.open(image_path) as image:
                prompt = self._get_prompt()
                response = self.model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            st.error(f"Error analyzing ingredients: {str(e)}")
            return None

    @staticmethod
    def _get_prompt() -> str:
        """
        Get the prompt for ingredient analysis.

        Returns:
            str: Formatted prompt for the AI model
        """
        return """
        Act as a food expert.
        Get all the ingredients from this image if any,
        if not found then give not found any,
        now for each ingredient check if it is safe or not,
        sort them by safe and unsafe, also how it is safe and if unsafe then why.
        Do not add comments or additional information.

        Your output should be in following markdown example format:
        ### Unsafe ingredients:
        - **Ingredient 1**    Health Benefits of ingredient 1
        - **Ingredient 2**    Health Benefits of ingredient 2
        ...
        ### Safe ingredients:
        - **Ingredient 3**    Health risk of ingredient 3
        - **Ingredient 4**    Health risk of ingredient 4
        ...
        ### Comments:
        Add some comment if it is safe or unsafe
        """


def extract_ingredients_with_gemini(image_path: str) -> Optional[str]:
    """
    Convenience function to extract ingredients from an image.

    Args:
        image_path: Path to the image file

    Returns:
        Optional[str]: Analysis results or None if extraction fails
    """
    extractor = IngredientExtractor()
    return extractor.extract_ingredients(image_path)
