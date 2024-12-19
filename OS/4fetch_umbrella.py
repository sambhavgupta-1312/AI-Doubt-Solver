import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer, util
import torch

with open('OS/umbrella_embeddings.pkl', 'rb') as f:
    umbrella_embeddings = pickle.load(f)

umbrella_data = pd.read_csv('data/topic_with_desc.csv')

def map_to_umbrella_topic(extracted_topic, umbrella_embeddings, umbrella_data):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    extracted_topic_embedding = model.encode([extracted_topic], convert_to_tensor=True)
    cosine_similarities = util.pytorch_cos_sim(extracted_topic_embedding, umbrella_embeddings)
    most_relevant_umbrella_idx = torch.argmax(cosine_similarities).item()

    # Retrieve the broader umbrella topic, its description, and keywords
    umbrella_topic = umbrella_data['Topic'].iloc[most_relevant_umbrella_idx]
    umbrella_description = umbrella_data['Description'].iloc[most_relevant_umbrella_idx]
    umbrella_keywords = umbrella_data['Keywords'].iloc[most_relevant_umbrella_idx]

    return umbrella_topic, umbrella_description, umbrella_keywords

extracted_topic = "Deadlocks"
umbrella_topic_info = map_to_umbrella_topic(extracted_topic, umbrella_embeddings, umbrella_data)
print("Umbrella Topic:", umbrella_topic_info)
