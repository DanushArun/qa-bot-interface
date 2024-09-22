# QA Bot Interface Documentation

## Model Architecture

The QA Bot Interface uses a Retrieval-Augmented Generation (RAG) approach, combining the following components:

1. Document Embedding: SentenceTransformer model ('all-MiniLM-L6-v2')
2. Document Storage: In-memory Python lists
3. Retrieval: Cosine similarity search
4. Answer Generation: Cohere's language model

## Retrieval Approach

1. Document Processing: PDF text is extracted and embedded using SentenceTransformer.
2. Storage: Embeddings and original text are stored in memory.
3. Retrieval: When a query is received, it's embedded and compared to stored document embeddings using cosine similarity.
4. The most relevant document segment is retrieved based on similarity scores.

## Generative Response Creation

1. The retrieved document segment is used as context for the Cohere language model.
2. A prompt is constructed combining the context and user question.
3. Cohere's API generates a response based on this prompt.
4. The generated answer is returned to the user.

## Challenges and Solutions

1. Pinecone Integration: Initially planned to use Pinecone for vector storage, but due to account limitations, switched to in-memory storage.
2. PDF Processing: Implemented PyPDF2 for robust PDF text extraction.
3. Error Handling: Added comprehensive error handling to manage potential issues with document processing or API calls.

## Future Improvements

1. Implement persistent storage for document embeddings.
2. Enhance retrieval with more sophisticated algorithms (e.g., semantic search).
3. Improve answer generation with fine-tuned models or prompt engineering.
4. Add support for multiple document formats beyond PDF.
