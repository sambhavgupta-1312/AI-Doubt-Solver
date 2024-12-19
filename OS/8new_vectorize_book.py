from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from tqdm import tqdm
import re
import sys

print("Starting the vectorization process...")


# Initialize the Qdrant client
url = "http://localhost:6333"  # Qdrant server URL
try:
    client = QdrantClient(url=url)
    if "1books" in client.get_collections().collections:
        print("Collection '1books' already exists.")
        user_input = input("Do you want to proceed with training this data? (Y/N): ").strip().lower()
        if user_input == "Y":
            print("Proceeding with training...")
        elif user_input == "N":
            print("Terminating program and exiting Qdrant.")
            client.close()
            sys.exit(0)
        else:
            print("Invalid input. Terminating program.")
            client.close()
            sys.exit(1)
    else:
        client.create_collection(
            collection_name="1books",
            vectors_config=VectorParams(size=384, distance=Distance.DOT)  # size = expected vector length
        )
        print("Collection '1books' created successfully.")
    print("Starting the training process...")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)  # Exit the program with an error code



# Load the OS subject book in PDF format
print("Loading PDF file...")

def clean_page_text(page_text):
    page_text = re.sub(r"^\s*\d+\s*$", "", page_text)  # Remove standalone page numbers like '4'
    page_text = re.sub(r"Chapter \d+.*", "", page_text)  # Remove chapter headers like 'Chapter 1 Introduction'
    # Remove figures
    page_text = re.sub(r"Figure \d+\.\d+.*", "", page_text)
    # Remove short sentences (3-4 words)
    sentences = page_text.split("\n")
    filtered_sentences = [sentence for sentence in sentences if len(sentence.split()) > 4]
    cleaned_text = "\n".join(filtered_sentences)

    return cleaned_text.strip()
def preprocess_pdf(raw_docs, start_page=31):
    processed_docs = []
    for i, doc in enumerate(raw_docs):
        # Skip pages before the start_page
        if i + 1 < start_page:
            continue

        cleaned_text = clean_page_text(doc.page_content)
        if cleaned_text:
            processed_docs.append(Document(page_content=cleaned_text, metadata=doc.metadata))
    return processed_docs

loader = PyPDFLoader("data/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf")
raw_docs = loader.load()
docs = preprocess_pdf(raw_docs)
print(f"PDF loaded successfully. Total pages: {len(docs)}")

# Split the document into smaller chunks for efficient vectorization
print("\nSplitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(docs)
print(f"Document splitting complete. Total chunks: {len(documents)}")

# Initialize HuggingFace BGE embeddings
model_name = "BAAI/bge-small-en"
print(f"\nInitializing HuggingFace BGE embeddings with model: {model_name}")
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
print("Embeddings model initialized successfully")


#establishing vector store
db = Qdrant(client=client, embeddings=embeddings, collection_name="1books")
print("\nCreating vector store...")
batch_size = 32
total_batches = (len(documents)-1)//batch_size + 1
print(f"Total number of batches to process: {total_batches}")

for i in tqdm(range(0, len(documents), batch_size), desc="Processing document chunks"):
    batch = documents[i:i + batch_size]
    db.add_documents(documents=batch)
    current_batch = i//batch_size + 1
    print(f"Batch {current_batch}/{total_batches} completed")
    if current_batch < total_batches:
        print(f"Progress: {(current_batch/total_batches)*100:.2f}% complete")

print("\nVectorization complete! Vectors stored in Qdrant database.")