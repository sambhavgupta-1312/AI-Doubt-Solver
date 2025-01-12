import streamlit as st
from OS.similarity_function import find_most_similar_questions

# Styling
st.markdown(
    """
    <style>
        body {
            background-color: black;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: white !important;
            color: black !important;
        }
        .stSlider {
            background-color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown(
        '<h1 style="color: #E74C3C;">OS Question Similarity Finder</h1>',
        unsafe_allow_html=True
    )
    st.write("Enter your query to find the most similar OS-related questions.")

    # Query input
    st.markdown('Enter your query here:')
    query = st.text_input(
        "this is hidden label",  # Keep label empty as it's now customized
        placeholder="Type your OS-related question...",
        label_visibility='hidden'
    )

    # Slider for similarity threshold
    st.markdown('Set the threshold value up to which you want similar questions')
    similarity_threshold = st.slider(
        "this is hidden label", 0.1, 1.0, 0.3, step=0.1,
        label_visibility='hidden'
    )

    # Find similar questions button
    if st.button("Find Similar Questions"):
        if query.strip() == "":
            st.error("Please enter a valid query.")
        else:
            similar_questions = find_most_similar_questions(query, similarity_threshold)
            
            if isinstance(similar_questions, str):
                st.warning(similar_questions)
            else:
                st.markdown(
                    '<h3 style="color: #E74C3C;">Hey, though your query is solved but you may have doubt in these similar variations to your problem!!:</h3>',
                    unsafe_allow_html=True
                )
                for i, (question, topic) in enumerate(similar_questions, start=1):
                    st.write(f"**{i}. Question:** {question}")
                    st.write(f"**Topic:** {topic}")

