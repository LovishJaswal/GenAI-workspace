## Setup Instructions

- This notebook uses the Hugging Face embedding model `sentence-transformers/all-mpnet-base-v2`.
- Make sure you have a Hugging Face account and access token.
- Add your Hugging Face token to the notebook's **Secrets** before running the notebook.
- Ensure that access to the secret key is enabled.
- The project uses a dataset containing **50 songs**, each with metadata and a detailed description for semantic search.
- Run all notebook cells sequentially to build the vector database and start searching for songs using natural language queries.

### Prerequisites

- Hugging Face Access Token (stored in Colab Secrets)
- Access to the embedding model: `sentence-transformers/all-mpnet-base-v2`

### Dataset

The project uses a dataset of **50 songs** containing:
- Song Name
- Artist
- Genre
- Mood
- Tempo
- Language
- Release Year
- Description

### Running the Project

1. Add your Hugging Face access token to **Colab Secrets** and grant notebook access.
2. Upload the provided `songs_dataset_50_final.json` dataset.
3. Run all notebook cells in order.
4. Enter a natural language query (e.g., *"Suggest energetic Punjabi songs with confident vibes"*).
5. The system retrieves the **Top 5 semantically similar songs** using ChromaDB and Hugging Face embeddings.


### How Embeddings and the Vector Database Were Used

This project uses embeddings and a vector database to build a semantic music recommendation system. Unlike traditional keyword-based search, embeddings convert text into high-dimensional numerical vectors that capture the semantic meaning and context of the content. Each song in the dataset contains metadata such as the song name, artist, genre, mood, tempo, language, release year, and a detailed description. These fields were combined into a single document for each song before generating embeddings.

The documents were processed using the Hugging Face embedding model sentence-transformers/all-mpnet-base-v2, which generated a vector representation for every song. Songs with similar meanings, themes, moods, or musical characteristics are positioned closer together in the vector space. These embeddings, along with their metadata, were stored in a Chroma vector database, enabling efficient retrieval.

When a user enters a natural language query such as "Suggest energetic Punjabi songs with confident vibes" or "Recommend romantic Hindi songs for a long drive", the query is converted into an embedding using the same model. Chroma then performs a nearest-neighbor similarity search by comparing the query embedding with the stored song embeddings. The comparison is based on a vector similarity or distance metric (such as cosine similarity or an equivalent distance measure, depending on the vector store configuration), allowing the system to retrieve songs that are semantically closest to the user's request rather than relying on exact keyword matches.

Finally, the system returns the top five most relevant songs along with their metadata, including the song name, artist, genre, mood, and similarity score. This semantic search approach produces recommendations that are more accurate, context-aware, and capable of understanding the user's intent beyond simple keyword matching.

![alt text](image.png)