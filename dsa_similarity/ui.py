import time
import streamlit as st
from dsa_similarity.Coding_Problems_Functionalities import (
    data,
    find_similar_questions,
    find_similar_topics,
)

def main():
    st.markdown(
        '<h1 style="color: #E74C3C;">Question and Topic Similarity Finder</h1>',
        unsafe_allow_html=True
    )

    # User input
    search_type = st.radio("Search by:", ("Question", "Topic"))

    if search_type == "Question":
        user_question = st.text_input("label is not visible", placeholder='Enter your question', label_visibility='hidden')
        if st.button("Find"):
            if user_question:
                with st.spinner("Fetching similar questions..."):
                    time.sleep(1)
                    similar_questions = find_similar_questions(user_question)
                    if similar_questions is not None:
                        st.subheader("Similar Questions:")
                        st.table(
                            similar_questions[["title", "tags"]].reset_index(drop=True)
                        )
                    else:
                        st.write(
                            "No highly similar questions found. This question appears to be new."
                        )
            else:
                st.error("Please enter a question to find similar questions.")

    else:
        user_topic = st.text_input("this label is not visible",placeholder='Enter your query topic', label_visibility='hidden')
        if st.button("Find"):
            if user_topic:
                with st.spinner("Searching for related topics..."):
                    time.sleep(1)
                    similar_topics = find_similar_topics(
                        user_topic
                    )  # Plural: similar_topics
                    if similar_topics:
                        st.write(f"Most similar topics found: {', '.join(similar_topics)}")
                        filtered_data = data[
                            data["topicTags"].apply(
                                lambda tags: any(topic in tags for topic in similar_topics)
                            )
                        ]
                        st.subheader("Questions related to the topics:")
                        if not filtered_data.empty:
                            st.table(
                                filtered_data[["title", "topicTags"]]
                                .reset_index(drop=True)
                                .head(5)  # Limit the results to top 5
                            )
                        else:
                            st.write("No questions found for the matched topics.")
                    else:
                        st.write("No similar topics found. This topic appears to be new.")
            else:
                st.error("Please enter a topic to find related questions.")
