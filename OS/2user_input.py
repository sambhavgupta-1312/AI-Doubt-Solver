import pandas as pd
import pickle
from sentence_transformers import util, SentenceTransformer
import torch

with open('OS/question_embeddings.pkl', 'rb') as f:
    stored_embeddings = pickle.load(f)

data = pd.read_csv('os_compare.csv')
model = SentenceTransformer('all-MiniLM-L6-v2')  #all-MPNet-base-v2

def find_most_similar_question(query, stored_embeddings, data, similarity_threshold):

    query_embedding = model.encode([query], convert_to_tensor=True)
    cosine_similarities = util.pytorch_cos_sim(query_embedding, stored_embeddings)
    most_similar_question_idx = torch.argmax(cosine_similarities).item()
    max_similarity = torch.max(cosine_similarities).item()
    #implementing fallback
    if max_similarity < similarity_threshold:
        return "No close match found. Please clarify your query or give the topic name."
    else:
        return data['corr_topic'].iloc[most_similar_question_idx]

user_input = "How does memory allocation work in operating systems?"

similar_topic_or_fallback = find_most_similar_question(user_input, stored_embeddings, data, 0.3)
print("Most Similar Question's Topic:", similar_topic_or_fallback)
