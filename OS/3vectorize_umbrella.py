from sentence_transformers import SentenceTransformer
import pandas as pd
import pickle

umbrella_data = pd.read_csv('data/topic_with_desc.csv')

model = SentenceTransformer('all-MiniLM-L6-v2') #all-MPNet-base-v2

umbrella_data['combined'] = umbrella_data['Topic'] + ' ' + umbrella_data['Description'] + ' ' + umbrella_data['Keywords']

umbrella_embeddings = model.encode(umbrella_data['combined'].tolist(), convert_to_tensor=True)

with open('OS/umbrella_embeddings.pkl', 'wb') as f:
    pickle.dump(umbrella_embeddings, f)
# with open('OS/umbrella_data.pkl', 'wb') as f:
#     pickle.dump(umbrella_data, f)
