import streamlit as st
import cohere
from sentence_transformers import SentenceTransformer
import PyPDF2
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

co = cohere.Client(os.getenv('COHERE_API_KEY'))

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

documents = []
embeddings = []

def process_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def embed_and_store(text):
    try:
        embedding = model.encode(text)
        documents.append(text)
        embeddings.append(embedding)
        st.success("Document processed and stored successfully!")
    except Exception as e:
        st.error(f"An error occurred while processing the document: {str(e)}")
        print(f"Detailed error: {e}")

def retrieve(query, top_k=1):
    query_embedding = model.encode(query)
    scores = [np.dot(query_embedding, doc_embedding) for doc_embedding in embeddings]
    top_indices = np.argsort(scores)[-top_k:][::-1]
    return [documents[i] for i in top_indices]

def generate_answer(question, context):
    try:
        prompt = f"Context: {context[0]}\n\nQuestion: {question}\nAnswer:"
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            stop_sequences=["\n"]
        )
        return response.generations[0].text.strip()
    except Exception as e:
        st.error(f"An error occurred while generating the answer: {str(e)}")
        print(f"Detailed error: {e}")
        return "I'm sorry, I couldn't generate an answer at this time."

def answer_question(question):
    context = retrieve(question)
    if context:
        answer = generate_answer(question, context)
        return answer, context[0]
    else:
        return "No relevant information found.", ""

def main():
    st.title("Interactive QA Bot")
    st.write("Upload a PDF document and ask questions about its content.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        with st.spinner("Processing document..."):
            document_text = process_pdf(uploaded_file)
            embed_and_store(document_text)

        user_question = st.text_input("Ask a question about the document:")

        if user_question:
            with st.spinner("Generating answer..."):
                answer, context = answer_question(user_question)
            
            st.subheader("Retrieved Document Segment:")
            st.write(context if context else "No relevant segment found.")
            
            st.subheader("Generated Answer:")
            st.write(answer)

if __name__ == "__main__":
    main()
