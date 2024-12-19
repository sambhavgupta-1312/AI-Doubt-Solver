import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import requests
from bs4 import BeautifulSoup
import pickle
from leetscrape import GetQuestion

# Load the dataset
def load_dataset():
    return pd.read_csv("dsa_data/leetcode_mod.csv")

def load_embeddings(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)
    
# Semantic search for problem statement
def semantic_search_problem_statement(user_query, problem_statement_embeddings, df, threshold=0.60):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([user_query])
    similarities = np.dot(problem_statement_embeddings, query_embedding.T).flatten()
    best_match_idx = np.argmax(similarities)
    if similarities[best_match_idx] >= threshold:
        return df.iloc[best_match_idx]['titleslug']
    return None

# Semantic search for question name
def semantic_search_question_name(user_query, title_embeddings, df, threshold=0.75):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([user_query])
    similarities = np.dot(title_embeddings, query_embedding.T).flatten()
    best_match_idx = np.argmax(similarities)
    if similarities[best_match_idx] >= threshold:
        return df.iloc[best_match_idx]['titleslug']
    return None

# Fetch hints for a given titleslug
def fetch_hints(titleslug):
    if not titleslug:
        return ["No hints available."]
    try:
        question = GetQuestion(titleSlug=titleslug).scrape()
        return question.Hints if question.Hints else ["No hints available."]
    except Exception as e:
        return [str(e)]

# Fetch coding platform (LeetCode editor link)
def fetch_coding_platform(titleslug):
    query = f"leetcode problems {titleslug}"
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    first_result = soup.find('div', class_='tF2Cxc')
    if first_result:
        link = first_result.find('a')['href']
        return f"You are advised to first solve this problem based on the hint given. Click on the link below to go to the editor:\n{link}"
    return "Unable to fetch coding platform link."

# Fetch solution links
def fetch_solution(titleslug):
    query = f"gfg {titleslug}"
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    first_result = soup.find('div', class_='tF2Cxc')
    if first_result:
        link = first_result.find('a')['href']
        return f"Solution link:\n{link}"
    return "Unable to fetch solution link."