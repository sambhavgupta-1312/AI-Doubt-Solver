import streamlit as st
from qna import (
    load_dataset,
    load_embeddings,
    semantic_search_problem_statement,
    semantic_search_question_name,
    fetch_hints,
    fetch_coding_platform,
    fetch_solution,
)

df = load_dataset()
problem_embeddings= load_embeddings('dsa/problem_statement_embeddings.pkl')
title_embeddings= load_embeddings('dsa/title_embeddings.pkl')

st.title("DSA Question Helper")

# User Input
option = st.selectbox(
    "How would you like to ask the question?",
    ["1. Full Problem Statement", "2. Question Name"]
)

if option == "1. Full Problem Statement":
    input_statement = st.text_area("Enter the full problem statement:")
    if st.button("Search"):
        titleslug = semantic_search_problem_statement(input_statement, problem_embeddings, df)
        if titleslug:
            st.success(f"Found question: {titleslug}")
            
            # Fetch Hints
            hints = fetch_hints(titleslug)
            st.subheader("Hints:")
            for hint in hints:
                st.text(hint)
            
            # Fetch Coding Platform Link
            coding_platform = fetch_coding_platform(titleslug)
            st.subheader("LeetCode Editor:")
            st.text("You are advised to first solve this problem based on the hints provided.")
            if "http" in coding_platform:
                st.markdown(
                    f"### [Click here to solve in LeetCode Editor]({coding_platform})",
                    unsafe_allow_html=True,
                )
            else:
                st.write(coding_platform)
            
            # Fetch Solution Link
            solution = fetch_solution(titleslug)
            st.subheader("Solution:")
            if "http" in solution:
                st.markdown(
                    f"### [Click here to view the solution]({solution})",
                    unsafe_allow_html=True,
                )
            else:
                st.write(solution)
        else:
            st.error("No matching question found.")

elif option == "2. Question Name":
    input_name = st.text_input("Enter the name of the question:")
    if st.button("Search"):
        titleslug = semantic_search_question_name(input_name,title_embeddings, df)
        if titleslug:
            st.success(f"Found question: {titleslug}")
            
            # Fetch Hints
            hints = fetch_hints(titleslug)
            st.subheader("Hints:")
            for hint in hints:
                st.text(hint)
            
            # Fetch Coding Platform Link
            coding_platform = fetch_coding_platform(titleslug)
            st.subheader("LeetCode Editor:")
            st.text("You are advised to first solve this problem based on the hints provided.")
            if "http" in coding_platform:
                st.markdown(
                    f"### [Click here to solve in LeetCode Editor]({coding_platform})",
                    unsafe_allow_html=True,
                )
            else:
                st.write(coding_platform)
            
            # Fetch Solution Link
            solution = fetch_solution(titleslug)
            st.subheader("Solution:")
            if "http" in solution:
                st.markdown(
                    f"### [Click here to view the solution]({solution})",
                    unsafe_allow_html=True,
                )
            else:
                st.write(solution)
        else:
            st.error("No matching question found.")