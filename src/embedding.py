from typing import List,Any
from  langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import numpy as np
from src.data_loader import load_all_documents

class EmbeddingPipeline:
    def __init__(self,model_name:str="all-MiniLM-L6-v2",chunk_size:int=1000,chunk_overlap:int=200):
        self.chunk_size=chunk_size
        self.chunk_overlap=chunk_overlap
        self.model = SentenceTransformer(model_name)

    def chunk_documents(self,documents:List[str]) -> List[str]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks=text_splitter.split_documents(documents)
        return chunks

    def embed_chunks(self,chunks:List[Any])->np.ndarray:
        texts = [chunk.page_content for chunk in chunks]
        embedding = self.model.encode(texts,show_progress_bar=True)
        return embedding
    
    
# if __name__ == "__main__":

#     docs = load_all_documents("data")
#     emb = EmbeddingPipeline()
#     chunks = emb.chunk_documents(docs)
#     embeddings = emb.embed_chunks(chunks)
#     print("[INFO] Example embedding:", embeddings[0] if len(embeddings) > 0 else None)