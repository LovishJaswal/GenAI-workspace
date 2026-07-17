# 🎵 Semantic Music Recommendation System

An AI-powered music recommendation system that uses **sentence embeddings** and a **vector database** to recommend songs based on the meaning of a user's query rather than simple keyword matching.

This project demonstrates how semantic search can be combined with structured metadata filtering to build an intelligent and customizable recommendation system.

---

# 🚀 Project Evolution

## Version 1 — Semantic Search Recommendation System

### Features

- Semantic music recommendation using sentence embeddings
- Natural language queries
- Hugging Face embedding model (`sentence-transformers/all-mpnet-base-v2`)
- Chroma Vector Database
- Top 5 semantic recommendations
- Console-based interface

---

### Setup Instructions

- This notebook uses the Hugging Face embedding model `sentence-transformers/all-mpnet-base-v2`.
- Make sure you have a Hugging Face account and access token.
- Add your Hugging Face token to the notebook's **Secrets** before running the notebook.
- Ensure that access to the secret key is enabled.
- The project uses a dataset containing **50 songs**, each with metadata and a detailed description for semantic search.
- Run all notebook cells sequentially to build the vector database and start searching for songs using natural language queries.

---

### Prerequisites

- Hugging Face Access Token (stored in Colab Secrets)
- Access to the embedding model:
  ```
  sentence-transformers/all-mpnet-base-v2
  ```

---

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

---

### Running Version 1

1. Add your Hugging Face access token to **Colab Secrets**.
2. Upload `songs_dataset_50_final.json`.
3. Run every notebook cell sequentially.
4. Enter a natural language query.

Example:

```
Suggest energetic Punjabi songs with confident vibes
```

5. The system retrieves the **Top 5 semantically similar songs**.

---

## Version 1 Workflow

```text
                 User Query
                      │
                      ▼
        Sentence Embedding Model
                      │
                      ▼
            Chroma Vector Database
                      │
                      ▼
        Semantic Similarity Search
                      │
                      ▼
          Top 5 Recommended Songs
```

---

### How Version 1 Works

Version 1 uses embeddings and a vector database to build a semantic music recommendation system.

Each song in the dataset contains metadata including:

- Song Name
- Artist
- Genre
- Mood
- Tempo
- Language
- Release Year
- Description

These fields are combined into a single document before generating embeddings.

The Hugging Face model

```
sentence-transformers/all-mpnet-base-v2
```

converts every song into a dense vector representation.

These vectors are stored inside **ChromaDB**, enabling efficient semantic similarity search.

When a user enters a natural language query such as

```
Suggest energetic Punjabi songs with confident vibes
```

or

```
Recommend romantic Hindi songs for a long drive
```

the query is embedded using the same embedding model.

ChromaDB compares the query embedding against all stored song embeddings and retrieves the most semantically similar songs using vector similarity.

Finally, the system returns the Top 5 recommendations along with:

- Song Name
- Artist
- Genre
- Mood
- Similarity Score

This approach understands the **meaning** of a query rather than relying only on exact keyword matching.

---

# 🚀 Version 2 — Hybrid Semantic Recommendation System

Version 2 improves the original project by combining **semantic retrieval** with **metadata filtering**.

Instead of directly returning the nearest semantic matches, the system first retrieves candidate songs using embeddings and then filters them according to the user's selected preferences.

---

## New Features

- Interactive Gradio Interface
- Genre Filter
- Language Filter
- Mood Filter
- Release Year Filter
- Dynamic Dropdown Generation
- Hybrid Recommendation Pipeline
- Improved User Experience

---

## Running Version 2

1. Add your Hugging Face access token.
2. Upload `songs_dataset_50_final.json`.
3. Run the notebook.
4. Launch the Gradio application.
5. Enter a natural language query.
6. Apply optional filters.
7. Receive personalized recommendations.

Example query:

```
Suggest relaxing songs for studying
```

Example filters:

```
Genre        : Pop
Language     : English
Mood         : Romantic
Released After : 2015
```

---

## Version 2 Workflow

```text
                 User Query
                      │
                      ▼
        Sentence Embedding Model
                      │
                      ▼
            Chroma Vector Database
                      │
                      ▼
        Semantic Similarity Search
             (Top 10 Candidates)
                      │
                      ▼
            Metadata Filtering
     (Genre • Language • Mood • Year)
                      │
                      ▼
          Top 5 Recommended Songs
                      │
                      ▼
               Gradio Interface
```

---

# What Improved in Version 2?

| Version 1 | Version 2 |
|------------|-----------|
| Pure semantic search | Hybrid recommendation system |
| Console-based interface | Interactive Gradio interface |
| No filtering | Genre, Language, Mood & Release Year filtering |
| Direct Top 5 retrieval | Retrieve Top 10 → Filter → Return Top 5 |
| Query only | Query + Structured Preferences |
| Less user control | Highly customizable recommendations |

---

# Why Version 2 Performs Better

Semantic search understands the meaning behind a user's request.

However, semantic search alone cannot always enforce explicit preferences.

For example, if a user searches for

```
Romantic songs
```

the semantic search may retrieve songs from different languages and genres because they share similar meanings.

Version 2 solves this limitation.

The recommendation pipeline now consists of two stages:

1. Semantic Retrieval
2. Metadata Filtering

Example:

### Query

```
Romantic songs
```

### Filters

```
Genre = Bollywood

Language = Hindi

Mood = Romantic

Released After = 2022
```

The system first retrieves semantically similar songs from ChromaDB.

It then removes every song that does not satisfy the selected filters.

This produces recommendations that satisfy **both semantic relevance and user-defined constraints**, making the results significantly more accurate and personalized.

---

# Technologies Used

- Python
- LangChain
- HuggingFace Embeddings
- ChromaDB
- Gradio
- JSON

---

# Project Structure

```text
Semantic-Music-Recommendation/
│
├── songs_dataset_50_final.json
├── songs_db/
├── music_recommendation.ipynb
├── README.md
└── requirements.txt
```

---

# Example Output

```text
🎵 Recommendation 1

Song Name       : Kesariya
Artist          : Arijit Singh
Genre           : Bollywood
Mood            : Romantic
Language         : Hindi
Release Year     : 2022

--------------------------------------------------

🎵 Recommendation 2

Song Name       : Apna Bana Le
Artist          : Arijit Singh
Genre           : Bollywood
Mood            : Romantic
Language         : Hindi
Release Year     : 2022
```

---

# Future Improvements

- Spotify API Integration
- Album Cover Display
- Audio Preview
- Artist Filter
- Tempo Filter
- Larger Music Dataset
- Hybrid Keyword + Semantic Search
- Personalized Recommendations
- Playlist Generation

---

# Author

**Lovish**

Built to explore semantic search, vector databases, embeddings, LangChain, ChromaDB, and AI-powered recommendation systems.