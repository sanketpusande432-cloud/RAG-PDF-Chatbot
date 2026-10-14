# RAG-Based PDF Question Answering Chatbot

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot developed using Python, Streamlit, LangChain, ChromaDB, and Groq API.

The chatbot answers user questions using information extracted from a PDF document.

## Technologies Used
- Python
- Streamlit
- LangChain
- ChromaDB
- Groq API
- PyPDF2

## Features
- Extracts text from a PDF document.
- Splits extracted text into smaller chunks.
- Stores document chunks in ChromaDB.
- Retrieves relevant information based on user questions.
- Generates answers using a Large Language Model (LLM).
- Displays retrieved source content.
- Maintains conversation history during the session.

## Project Files
- `app.py` — Streamlit chatbot interface
- `llm.py` — Groq LLM integration
- `response.py` — Question answering and response generation
- `vectordb.py` — PDF processing and vector database
- `requirements.txt` — Required Python libraries

## How to Run
1. Download or clone this repository.
2. Install the required libraries:

   `pip install -r requirements.txt`

3. Create a `.env` file and add your Groq API key:

   `GROQ_API_KEY=your_api_key`

4. Place the sample PDF in the project folder.
5. Run the application:

   `streamlit run app.py`

## Sample Questions
- What is Python?
- What is the difference between a list and a tuple?
- What are Python functions?

## Future Enhancements
- Allow users to upload PDFs directly.
- Support multiple PDF documents.
- Improve source references and retrieval accuracy.

## Conclusion
This project demonstrates how Retrieval-Augmented Generation can combine document retrieval with an LLM to answer questions using information from a PDF.