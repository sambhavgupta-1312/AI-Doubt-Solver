import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
data = pd.read_csv("dsa_data/data.csvquestions.csv")
leetcode_mod = pd.read_csv("dsa_data/leetcode_mod.csv")


# Convert topicTags from string to list for 'data.csv'
def parse_tags(tag_string):
    if isinstance(tag_string, str):
        try:
            import ast

            return ast.literal_eval(tag_string)
        except (ValueError, SyntaxError):
            return tag_string.split(",")
    return []  # If not a string, return empty list


data["topicTags"] = data["topicTags"].apply(parse_tags)

# Load pre-trained sentence transformer model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)  

# Create embeddings for existing data
data_titles = list(leetcode_mod["title"])
title_embeddings = model.encode(data_titles)


# Helper function to find similar questions based on the user input question
def find_similar_questions(user_question):
    user_embedding = model.encode([user_question])
    similarities = cosine_similarity(user_embedding, title_embeddings).flatten()

    # Get top 5 most similar questions
    top_indices = np.argsort(similarities)[-5:][::-1]
    similar_questions = leetcode_mod.iloc[top_indices]

    # If the highest similarity score is too low, consider the question new
    if similarities[top_indices[0]] < 0.5:  # Adjust threshold as needed
        return None
    return similar_questions


# Helper function to find similar topics
def find_similar_topics(user_topic):
    # Extract unique topics from 'data.csv' (topicTags column)
    topics = list(
        set(tag for tags in data["topicTags"] for tag in tags)
    )  # Convert set to list
    topic_embeddings = model.encode(topics)

    user_embedding = model.encode([user_topic])
    similarities = cosine_similarity(user_embedding, topic_embeddings).flatten()

    # Sort topics by similarity and get top 5
    sorted_indices = np.argsort(similarities)[::-1]
    top_indices = sorted_indices[:5]  # Limit to top 5 topics
    top_topics = [topics[i] for i in top_indices]  # Get corresponding topics
    top_scores = similarities[top_indices]  # Get similarity scores for top topics

    # Filter topics with a similarity score below the threshold
    filtered_topics = [
        (topic, score) for topic, score in zip(top_topics, top_scores) if score >= 0.5
    ]

    if not filtered_topics:  # If no topics meet the threshold, return None
        return None
    return [topic for topic, _ in filtered_topics]  # Return only topic names
