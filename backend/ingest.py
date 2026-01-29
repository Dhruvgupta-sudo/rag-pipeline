from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FOLDER = os.path.join(BASE_DIR, "vectorstore")

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

    template = """Use the following pieces of context to answer the question at the end.
If the answer is not in the context, say "I do not have enough information to answer this question based on the provided documents." and do not try to make up an answer.

Context:
{context}

Question: {question}

Helpful Answer:"""

    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    
    return qa_chain

def main():
    qa_chain = get_rag_chain()
    query = "What is the main function of financial markets?"

    result = qa_chain.invoke(query)   # modern API

    print("\nANSWER:\n")
    print(result["result"])

    print("\nSOURCES:\n")
    for doc in result["source_documents"]:
        print(doc.metadata["source"], "page", doc.metadata["page"])

if __name__ == "__main__":
    main()
