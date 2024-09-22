# QA Bot Interface

## Overview
This project implements a Retrieval-Augmented Generation (RAG) model for a Question Answering (QA) bot. It uses Streamlit for the user interface, SentenceTransformer for embedding generation, and Cohere for text generation.

## Features
- PDF document upload and processing
- In-memory vector storage for document embeddings
- Cosine similarity search for relevant document retrieval
- Generative QA using Cohere's language model

## Setup Instructions
1. Clone this repository:
   ```
   git clone https://github.com/DanushArun/qa-bot-interface.git
   cd qa-bot-interface
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add your Cohere API key:
   ```
   COHERE_API_KEY=your_cohere_api_key_here
   ```

## Usage
1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open the provided URL in your web browser.
3. Upload a PDF document using the file uploader.
4. Ask questions about the document content in the text input field.

## Docker Setup
1. Build the Docker image:
   ```
   docker build -t qa-bot-interface .
   ```
2. Run the Docker container:
   ```
   docker run -p 8501:8501 qa-bot-interface
   ```
3. Open `http://localhost:8501` in your web browser.

## Components
- Streamlit: Provides the web interface for user interaction
- SentenceTransformer: Generates embeddings for document text and queries
- Cohere: Generates human-like responses based on retrieved context

## Limitations and Future Improvements
- Current implementation uses in-memory storage, which is not persistent
- Scaling to larger datasets may require integration with a vector database
- Improved error handling and user feedback could enhance the user experience

## License
MIT License
