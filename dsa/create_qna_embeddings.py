import pickle
from sentence_transformers import SentenceTransformer
import pandas as pd

# Create and store embeddings
def create_and_store_embeddings(filepath, problem_statement_output, title_output):
    df = pd.read_csv(filepath)
    
    # Initialize sentence transformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Generate embeddings
    print("Generating embeddings for problem statements...")
    problem_statement_embeddings = model.encode(df['problem_statement'].tolist(), show_progress_bar=True)
    print("Generating embeddings for titles...")
    title_embeddings = model.encode(df['title'].tolist(), show_progress_bar=True)
    
    # Save embeddings with pickle
    with open(problem_statement_output, 'wb') as ps_file:
        pickle.dump(problem_statement_embeddings, ps_file)
    with open(title_output, 'wb') as title_file:
        pickle.dump(title_embeddings, title_file)
    
    print("Embeddings successfully created and saved!")

# Specify filepaths
if __name__ == "__main__":
    dataset_filepath = 'leetcode_mod.csv'
    problem_statement_output = 'problem_statement_embeddings.pkl'
    title_output = 'title_embeddings.pkl'
    
    create_and_store_embeddings(dataset_filepath, problem_statement_output, title_output)
