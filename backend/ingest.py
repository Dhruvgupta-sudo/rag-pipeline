from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

DB_FOLDER = "vectorstore"

def get_rag_chain():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=DB_FOLDER,
        embedding_function=embeddings
    )

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.2
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    
    return qa_chain

def main():
    qa_chain = get_rag_chain()
    query = "What causes climate change?"

    result = qa_chain.invoke(query)   # modern API

    print("\nANSWER:\n")
    print(result["result"])

    print("\nSOURCES:\n")
    for doc in result["source_documents"]:
        print(doc.metadata["source"], "page", doc.metadata["page"])

if __name__ == "__main__":
    main()
