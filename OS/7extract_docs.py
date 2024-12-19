from langchain_community.document_loaders import PyPDFLoader

def extract_real_pages(file_path, real_page_numbers, offset):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    pdf_index_pages = [page + offset for page in real_page_numbers]
    return [doc for doc in docs if doc.metadata["page"] in pdf_index_pages]

file_path = "data/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf"
offset = 28

real_pages = input("Enter the real page numbers (comma-separated): ")
real_page_numbers = [int(page.strip()) for page in real_pages.split(",")]

filtered_docs = extract_real_pages(file_path, real_page_numbers, offset)

for doc in filtered_docs:
    print(f"Real Page {doc.metadata['page'] - offset}: {doc.page_content[:100]}...")
