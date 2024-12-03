"""
Streamlit application for analyzing ingredients in product images.
"""
from typing import Optional

import streamlit as st
from PIL import Image
import io

from gemini_ai import extract_ingredients_with_gemini


class IngredientAnalyzer:
    """Handles ingredient analysis."""

    @staticmethod
    def analyze_image(image_path: str) -> str:
        """
        Analyze the ingredients in the image.

        Args:
            image_path: Path to the image file

        Returns:
            str: Analysis results
        """
        return extract_ingredients_with_gemini(image_path)


class ImageProcessor:
    """Handles image processing and analysis in the Streamlit application."""

    def __init__(self) -> None:
        """Initialize the image processor with an ingredient analyzer."""
        self.analyzer = IngredientAnalyzer()

    @staticmethod
    @st.cache_data
    def process_image(image_bytes: bytes) -> Optional[str]:
        """
        Process the image and analyze its ingredients.

        Args:
            image_bytes: Raw image data in bytes

        Returns:
            Optional[str]: Analysis results or None if processing fails
        """
        try:
            with io.BytesIO(image_bytes) as image_buffer:
                temp_image_path = "temp_image.png"
                Image.open(image_buffer).convert("RGB").save(temp_image_path)
                return IngredientAnalyzer.analyze_image(temp_image_path)
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
            return None


def main() -> None:
    """Main function to run the Streamlit application."""
    st.title("Ingredient Analyzer")

    # Image source selection
    image_source = st.radio(
        "Choose image source:",
        ("Upload Image", "Capture from Camera"),
    )

    # Image input handling
    image_bytes = None
    if image_source == "Upload Image":
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=["jpg", "jpeg", "png"],
        )
        if uploaded_file is not None:
            image_bytes = uploaded_file.getvalue()
    else:
        camera_image = st.camera_input("Take a picture")
        if camera_image is not None:
            image_bytes = camera_image.getvalue()

    # Image processing and result display
    if image_bytes:
        processor = ImageProcessor()
        if result := processor.process_image(image_bytes):
            st.markdown(result)
        else:
            st.error("Failed to analyze the image. Please try again.")


if __name__ == "__main__":
    main()
