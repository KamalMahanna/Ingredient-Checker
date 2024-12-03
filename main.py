import streamlit as st
from PIL import Image
import io
from gemini_ai import extract_ingredients_with_gemini

class IngredientAnalyzer:
    @staticmethod
    @st.cache_data
    def analyze_image(image_bytes):
        with io.BytesIO(image_bytes) as image_buffer:
            temp_image_path = "temp_image.png"
            Image.open(image_buffer).convert("RGB").save(temp_image_path)
            result = extract_ingredients_with_gemini(temp_image_path)
        return result

def main():
    st.title("Ingredient Analyzer")

    image_source = st.radio(
        "Choose image source:",
        ("Upload Image", "Capture from Camera")
    )

    image_bytes = None
    if image_source == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image_bytes = uploaded_file.getvalue()
    else:
        camera_image = st.camera_input("Take a picture")
        if camera_image is not None:
            image_bytes = camera_image.getvalue()
    
    if image_bytes:   
        analyzer = IngredientAnalyzer()
        result = analyzer.analyze_image(image_bytes)
        if result:
            st.markdown(result)
        else:
            st.error("Failed to analyze the image. Please try again.")

if __name__ == "__main__":  
    main()
