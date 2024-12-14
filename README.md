# Healthy Checker

The Healthy Checker project helps users identify the safest and harmful ingredients in food items. It provides a comprehensive list of ingredients, allowing users to make informed dietary choices based on their preferences and restrictions.

You can try the project at the following link: [Ingredient Checker](https://ingredient-checker.streamlit.app/).

**Installing Manually**
===================

To manually install and set up the Streamlit application, follow these steps:

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/KamalMahanna/Ingredient-Checker.git
```

Move into the cloned repository directory:

```bash
cd Ingredient-Checker
```

### Step 2: Create the `.streamlit` Folder and `secrets.toml` File

Create a new folder named `.streamlit` in the root of the repository:

```bash
mkdir .streamlit
```

Inside the `.streamlit` folder, create a new file named `secrets.toml`.

```bash
touch .streamlit/secrets.toml
```

Add the following line to this file:

```
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key. If you don't have one, follow these steps to get a Gemini API key:

* Go to the [Google AI Studio website](https://aistudio.google.com/app/apikey) and sign up for an account.
* Log in to your account and navigate to the "API Keys" section.
* Click on "Create New Key" and follow the instructions.

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Finally, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This will start the application in your default web browser.
