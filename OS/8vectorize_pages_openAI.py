import openai
import os
import pickle
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

embeddings_dir = 'OS/topic_embeddings'
os.makedirs(embeddings_dir, exist_ok=True)

def vectorize_text_with_openai(text, topic_name):
    topic_embeddings_path = os.path.join(embeddings_dir, f"{topic_name}_embeddings.pkl")

    if not os.path.exists(topic_embeddings_path):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=16, 
            n=1, 
            logprobs=0 
        )

        embeddings = response['choices'][0]['text']

        with open(topic_embeddings_path, 'wb') as f:
            pickle.dump(embeddings, f)

        with open(os.path.join(embeddings_dir, 'topics_tracked.txt'), 'a') as f:
            f.write(f"{topic_name}\n")

    return topic_embeddings_path

# Example
sample_text = "Discuss the process management in operating systems."
topic_name = "Process Management"
embeddings_path = vectorize_text_with_openai(sample_text, topic_name)
print("Embeddings stored at:", embeddings_path)
