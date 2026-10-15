from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    store = FaissVectorStore("faiss_store")
    import os
    if not os.path.exists("faiss_store/faiss.index"):
        docs = load_all_documents("./rag/files/textfiles")
        store.build_from_documents(docs)
    else:
        store.load()
    #print(store.query("What is attention mechanism?", top_k=3))
    rag_search = RAGSearch()
    query = "Who is Alok"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)