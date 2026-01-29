# RAG Knowledge Assistant

This is a Retrieval-Augmented Generation (RAG) application that allows users to query a knowledge base created from PDF documents.
It consists of a Python FastAPI backend (using LangChain & ChromaDB) and a React frontend.

## Features

- **PDF Ingestion**: Parses PDFs and creates a vector store.
- **RAG Pipeline**: Retrieves relevant context and generates answers using Gemini.
- **Modern UI**: Clean, query-driven interface built with React.
- **Source Citation**: Displays the exact file and page number for every source used.

## Prerequisites

- **Python 3.10+**
- **Node.js 18+** & **npm**
- **Google API Key** (for Gemini)

## Installation

### 1. Backend Setup

Navigate to the root directory and create a virtual environment (if not already active):

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

**Configuration**:
Ensure you have your environment variables set up (e.g., `GOOGLE_API_KEY`) if required by the underlying LangChain setup (usually in `.env` or system env).

### 2. Frontend Setup

Navigate to the frontend directory and install dependencies:

```bash
cd frontend
npm install
```

## Usage

### 1. Ingest Data (First Run Only)

If you haven't created the vector database yet, run the creation script:

```bash
# From the root directory (with venv active)
python backend/createdb.py
```

This processes PDFs in `data/pdfs/` and saves the vector store to `vectorstore/`.

### 2. Start the Backend Server

Start the FastAPI server:

```bash
# From the root directory
uvicorn backend.api:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

### 3. Start the Frontend

In a new terminal, start the React development server:

```bash
cd frontend
npm run dev
```

Open the URL shown (usually `http://localhost:5173`) in your browser.

## Project Structure

```
rag1/
├── backend/
│   ├── api.py          # FastAPI application
│   ├── ingest.py       # RAG chain logic
│   ├── createdb.py     # Database creation script
│   └── vectorstore/    # ChromaDB storage
├── frontend/
│   ├── src/
│   │   ├── components/ # React components
│   │   ├── App.jsx     # Main frontend logic
│   │   └── index.css   # Styling
│   └── package.json
├── data/
│   └── pdfs/           # Input PDF documents
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## API Documentation

Once the backend is running, you can view the automatic API docs at:
`http://localhost:8000/docs`
