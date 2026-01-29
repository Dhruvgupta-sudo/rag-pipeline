from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.ingest import get_rag_chain
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class Source(BaseModel):
    file: str
    page: int

class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]

# Initialize chain on startup (or lazily)
chain = get_rag_chain()

@app.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    try:
        # Invoke the chain
        result = chain.invoke(request.question)
        
        answer = result["result"]
        source_docs = result.get("source_documents", [])
        
        sources = []
        for doc in source_docs:
            # Extract just the filename from the path if preferred, or keep full path
            # The user requested "filename — page X" format in UI, let's send what we have.
            # Assuming metadata has "source" and "page"
            file_path = doc.metadata.get("source", "Unknown file")
            page_num = doc.metadata.get("page", 0)
            # Normalize file path to just basename for cleaner UI? 
            # The prompt example showed "climate_change_report.pdf", so let's try to extract basename if it's a path.
            file_name = os.path.basename(file_path)
            
            sources.append(Source(file=file_name, page=page_num))
            
        return QueryResponse(answer=answer, sources=sources)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
