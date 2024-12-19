from sentence_transformers import SentenceTransformer
import pandas as pd
import pickle

data = pd.read_csv('data/os_compare.csv')

model = SentenceTransformer('all-MiniLM-L6-v2')  #all-MPNet-base-v2

question_embeddings = model.encode(data['question'].tolist(), convert_to_tensor=True)

with open('question_embeddings.pkl', 'wb') as f:
    pickle.dump(question_embeddings, f)
