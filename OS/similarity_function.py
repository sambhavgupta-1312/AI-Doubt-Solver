import pandas as pd
import pickle
from sentence_transformers import util, SentenceTransformer
import torch

with open('OS/question_embeddings.pkl', 'rb') as f:
    stored_embeddings = pickle.load(f)

data = pd.read_csv('data/os_compare.csv')
model = SentenceTransformer('all-MiniLM-L6-v2') 

def find_most_similar_questions(query, similarity_threshold):
    query_embedding = model.encode([query], convert_to_tensor=True)

    cosine_similarities = util.pytorch_cos_sim(query_embedding, stored_embeddings)

    top_k = 5
    top_k_indices = torch.topk(cosine_similarities, k=top_k).indices.squeeze(0).tolist()
    top_k_scores = torch.topk(cosine_similarities, k=top_k).values.squeeze(0).tolist()

    similar_questions = []
    for idx, score in zip(top_k_indices, top_k_scores):
        if score < similarity_threshold:
            break
        question = data['question'].iloc[idx]
        topic = data['corr_topic'].iloc[idx]
        similar_questions.append((question, topic))
        
    if not similar_questions:
        return "No close match found. Please clarify your query or give the topic name."

    return similar_questions
