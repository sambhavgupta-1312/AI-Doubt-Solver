from langchain_ollama import OllamaLLM
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient 
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def initialize_llm(model_name="llama2"):
    return OllamaLLM(model=model_name)

def create_prompt_template():
    return ChatPromptTemplate.from_template("""
    You are an AI assistant with expertise in Operating Systems. 
    Use the provided context from the book to answer the user's question in detail.
    Ensure your response is concise, accurate, and helpful.
    <context>
    {context}
    </context>
    Question: {input}
    Answer step by step:
    """)

def load_qdrant_retriever(qdrant_db_path, collection_name, k=3):
    try:
        model_name = "BAAI/bge-small-en"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': False}
        embeddings = HuggingFaceBgeEmbeddings(
                        model_name=model_name,
                        model_kwargs=model_kwargs,
                        encode_kwargs=encode_kwargs
                    )
        
        print("embeddings initialized success...")
        
        # Initialize the Chroma vector store
        client = QdrantClient(url=qdrant_db_path)
        vectorstore = Qdrant(client=client, collection_name=collection_name, embeddings=embeddings)
        return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})
    except Exception as e:
        print(f"Error loading Chroma retriever: {e}")
        return None  

def initialize_chains(llm, prompt_template, retriever):
    try:
        document_chain = create_stuff_documents_chain(llm, prompt_template)
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        return retrieval_chain
    except Exception as e:
        print(f"Error initializing chains: {e}")
        return None

def process_query(llm, retriever, query):
    prompt_template = create_prompt_template()
    retrieval_chain = initialize_chains(llm, prompt_template, retriever)
    try:
        response = retrieval_chain.invoke({"input": query})
        return response['answer']
    except Exception as e:
        print(f"Error generating answer: {e}")
        return None