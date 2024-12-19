import streamlit as st
from similarity_function import find_most_similar_questions

st.title("OS Question Similarity Finder")
st.write("Enter your query to find the most similar OS-related questions.")

query = st.text_input("Enter your query here:")

similarity_threshold = st.slider("Set the threshold value upto which you want similar questions", 0.1, 1.0, 0.3, step=0.1)

if st.button("Find Similar Questions"):
    if query.strip() == "":
        st.error("Please enter a valid query.")
    else:
        similar_questions = find_most_similar_questions(query, similarity_threshold)
        
        if isinstance(similar_questions, str):
            st.warning(similar_questions)
        else:
            st.subheader("Hey, though your query is solved but you may have doubt in these similar variations to your problem!!:")
            for i, (question, topic) in enumerate(similar_questions, start=1):
                st.write(f"**{i}. Question:** {question}")
                st.write(f"**Topic:** {topic}")
