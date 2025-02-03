# Recipe Generator

## Overview
The **Recipe Generator** is an AI-powered web application built with Streamlit. It helps users discover recipes based on ingredients they have or by providing a dish name to get step-by-step instructions. The app leverages **LangChain**, **FAISS**, and **ChatGroq** to retrieve and generate recipe recommendations.

## Features
- **Ingredient-based Recipe Suggestions:** Users can input available ingredients, and the app will suggest possible recipes.
- **Dish Name Lookup:** Users can enter a dish name to receive a step-by-step guide on how to prepare it.
- **AI-Powered Recipe Retrieval:** Utilizes a **retrieval-augmented generation (RAG) system** to fetch relevant recipes from a database.
- **Interactive Chat Interface:** Provides an intuitive chatbot experience for a seamless user journey.
- **Custom UI Styling:** Styled with custom CSS for an elegant and user-friendly design.

## Tech Stack
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-yellowgreen?logo=apache)
![LangChain](https://img.shields.io/badge/LangChain-Framework-orange?logo=fastapi)
![ChatGroq](https://img.shields.io/badge/ChatGroq-LLM-green?logo=openai)

## Installation

### Prerequisites
Make sure you have the following installed:
- Python (>=3.8)
- pip
- Virtual environment (optional but recommended)

### Clone the Repository
```sh
git clone https://github.com/yourusername/recipe-generator.git
cd recipe-generator
```

### Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate  # On Windows
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a **.env** file in the project root and add your API keys:
```sh
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

### Run the Application
```sh
streamlit run app.py
```

## Project Structure
```
recipe-generator/
│── app.py               # Main Streamlit application
│── scraped_recipes.json # JSON dataset of recipes
│── .env                 # Environment variables
│── requirements.txt     # List of dependencies
│── freefood.png         # Homepage image
└── README.md            # Project documentation
```

## Usage
1. **Home Page:** Click **"Get Started"** to access the chatbot.
2. **Chatbot Interface:** Type an ingredient or dish name in the chatbox.
3. **Recipe Generation:** The AI will suggest recipes based on your input.
4. **Navigation:** Click **"← Back to Home"** to return to the main screen.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or additional features.

## License
This project is licensed under the MIT License.

## Author
**Joseph Murasa Dushimimana**

For inquiries, reach out via:
- **Email:** dushimimanamurasajoseph@gmail.com
- **LinkedIn:** [Joseph Murasa Dushimimana](https://linkedin.com/in/dushimimana-murasa-joseph-7b5317247/)

